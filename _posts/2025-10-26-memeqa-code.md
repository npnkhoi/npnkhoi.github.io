---
layout: post
title: Implementation of MemeQA
tags: ml
---

Our group recently released the source code for the paper titled [“MemeQA: Holistic Evaluation for Meme Understanding”](https://aclanthology.org/2025.acl-long.927/), published at ACL’25. This codebase is designed to run experiments that answer certain research questions. Here I will report the engineering aspect of that codebase.

## Research context

The research project concerns Visual Question Answering, a much-demanded problem where a computer has to answer virtually any question about an image. For example, a kid may ask about the shape of a geometrical object in her math textbook, a tourist may ask about a building or a portion of the map, and a driver may ask about the thing he is seeing in his car. There are too many types of images to cover. In our project, we focused on memes, the types of images that contains a lot of cultural references and commonsense assumptions. The ability of SOTA vision language models (VLMs) to understanding these images is not well understood. Therefore, we ask:

(1) How can we design a challenging test suite to test VLMs on meme understanding? We need a large number of questions; and due to high cost of human labor, the process should be mostly automated.

(2) Once having the test suite, how well do the VLMs perform on it?

I will so how the implementation ideas to answer these two questions. Our full codebase is on [Github](https://github.com/npnkhoi/memeqa).

## Adversarial Filtering (AF)

For question 1, Adversarial Filtering (AF) was used. AF was introduced in 2018 by Zellers et al. in the paper [“Swag: A Large-Scale Adversarial Dataset for Grounded Commonsense Inference”](https://aclanthology.org/D18-1009/). The goal of AF is to *automate* the process of creating challenging *multiple-choice* questions for models. 

In a multiple choice question, there are 3 parts: the question text, the correct options, and the wrong options. Here, we assume the question text and the correct options are fixed (obtained from manual annotations). Then, the *difficulty* of answering the whole question depends on how *similar* the wrong options are to the correct ones, from the answerer’s perspective. AF maximizes this difficulty by (1) sampling a sufficiently large set of wrong options and (2) choosing the few most confusing wrong options to put in the question. Thanks to the power of LLMs, both parts can be done automatically. In particular, (1) is done by using a “generator” LLM to generate wrong options. Then, (2) is done by using a “discriminator” LLM to answer the resulting question (containing the generated wrong options) as best as it could. Depending on whether the discriminator answers correctly, we know whether the wrong options successfully confuse the discriminator models. 

AF runs per iterations. It starts with a set of “skeleton” questions that contain only the question text and the correct answers. At every iteration, for each question, the generator first generates the wrong options; then the discriminator answers the new question containing those wrong options. If the discriminator answers it correctly, we discard the current wrong options to generate new ones in later iterations. Otherwise, we deem the question sufficiently difficult. AF ends when the discriminator’s accuracy on the whole dataset stabilizes. Assuming the discriminator is representative of the target models we want to benchmark, we can assume that the resulting questions will be maximally challenging for the target models.

The core AF algorithm is in `src/af/af_base.py`. Below is the pseudo code:

```python
def af_run(questions: list[Question], generator, discriminator) -> list[Question]:
	NUM_ITER = 20 # we used a fixed number of iterations
	success, failed = [], questions
	
	# AF loop
	for _ in range(NUM_ITER):
		# generate
		new_questions = generator.generate(failed)
		# discriminate
		answers = discriminator.discriminate(new_questions)
		# update
		failed = []
		for q, a in zip(new_questions, answers):
			if correct(a, q):
				failed.append(q)
			else:
				success.append(q)
	
	return success + failed
		
```

For our problem, there are 11 types of questions, which has different requirements for the options. For example, the fill-in-the-blank questions require the options to make grammatical sense when being filled into the blank. And questions about “background knowledge to understand the meme” requires generating fact-like statements, while questions on the meme’s intents require generating statements about the meme’s intentions. Therefore, we wrote 11 different generators for those questions types. See their code in `src/af/*.py`.

Beside the main ideas above, a few more techniques were implemented to make the code either efficient or maintainable:

- OOP: Classes are `DiscriminatorAF`, `GeneratorAF`, `AFBase` and its 11 child classes `SomethingAF`. There are some cross inheritances, such as `DerivComp` (derivation completion) inherits `IntentComp` (intent completion).
- The discriminator and generator house actual VLMs inside them, handled with the `transformers` API. Those VLMs are lazy-loaded to save time during testing. Their encoding and decoding steps were handled explicitly[^1].
- Regarding hardware management, accelerate’s `auto` mode was sufficient. Two 24GB GPUs could contain both the generator model (Llama 3.1 8B) and the discriminator model (QWEN2-VL 7B).

[^1]: Transformers-based handling is now less relevant given LLM serving libraries such as `vllm`.

## Benchmarking VLMs

After AF, we ended up with over 9000 questions, enough not only for testing but also model training. For question 2, we run large training and inference jobs of popular VLMs to benchmark them. We tested with 6 models, divided into 2 groups:

- Group 1: ≤8B open-source models from HuggingFace— `Qwen2-VL-7B-Instruct` , `BLIP2-Flan-T5-xl`, `InstructBLIP-Vicuna-7B`, and `LLaVA-v1.5`
- Group 2: big models, called via external APIs — `QVQ-72B-Preview` (via Nebius) and `GPT-4o` (via OpenAI).

Each model in group 1 went through training on 7.2K examples in our training set. The training was done using the `peft` library, which performs LoRA fine-tuning on ~0.2% of the total model size. Our training loop was written explicitly in `torch` (see `src/train.py`). Under 16-bit precision, all of these models can be trained individually with two 24GB GPUs.

Evaluation was more straight-forward. For group 1, I continued to explicitly implemented with the `torch` library, as seen in `src/evaluate.py`. For group 2, I called inference services via the `openai` library (see `src/predict_gpt.py`)

## Remarks

**Training loop.** It’s worth to point out that, even though there is a popular API for LLM training called `Trainer`, I still wrote the training loop explicitly in `torch`. The reason was that, a few months before, I found out that `Trainer` did not have support for VLM training with custom validation metric. My findings were shared in [an earlier blog post]({%post_url 2024-10-06-trainer%}). It’s been exactly a year since that blog post, so I am hopeful that the support is in place now. The Trainer API is much cleaner to use.

**AF.** Our AF has two deviations from the original algorithm in Zellers et al. Firstly, instead of removing only the option with the lowest discriminator’s probability, we remove all of them because we did not access such probabilities. Secondly, to make sure later iterations yield novel options, we include the previous options in the prompt and command the model not to regenerate them. (In the original version, I think the authors relied on randomness to get novel options.)

**Structured outputs.** During that time, I was not familiar with constrained decoding APIs of transformers and openai library, so I discarded instances where the model did not return outputs in the right format. Now, `vllm` and `openai` both support that, so I now always obtain things in structured formats.

**QA.** The dataset is named after someone who I am deeply grateful to know and grow with. They will always be a part of me and my future successes.

## Footnotes
