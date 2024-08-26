---
layout: post
title: SelfCheckGPT -- a method to detect if an LLM is hallucinating
tags: ml
---

Hallucination in LLMs is the phenomenon of LLMs saying *factually wrong* things *confidently*. Such outputs may mislead users and lead to bad consequences in real life. This is a headache to AI product managers because they care about user trust, and hallucination damages that.

## How do we detect hallucinations? 

In a setting where we have access to all the facts, we can just do fact-checking every single thing the LLM produce. That is actually a whole method where a knowledge database is used to detect hallucination. However, it should be obvious to see that having a knowledge base that is able to fact-check everything is insanely impractical due to the amount of knkowledge the database have to collect and store.

We should notice that using a database is an *extrinsic* way to verify. That implies the existence of the *intrinsic* way, where we can just look at the LLM itself to detect hallucinations. More specifically, there are three ways to intrinsically do that:
- **White-box method**: accessing to the all hidden states of an LLM during the forward pass. This is similarly to scanning the brain to tell if a person is lying or crazy.
- **Grey-box method**: looking at the output token probabilities. This is similar to looking at how confidently a person pronouces each word.
- **Black-box method**: only looking at the output itself. This is similar to considering only the contents of the speech.

[SelfCheckGPT](http://arxiv.org/abs/2303.08896), a paper from Cambridge from October 2023, proposes a suite of black-box methods for doing this. They have been receiving 300 citations after less than a year, i.e., one academic citation every day.

## How SelfCheckGPT works

How do we check if a person is lying just by listen to what they say, not even how they say it? SelfCheckGPT authors choose to ask them multiple times and measure the *consistency* in the answers -- the more inconsistent they are, the more hallucinating the LLM is. This is just a theory and I am not sure if it has been proved before. It is based on intuition of the experts, who even formalize the inconsistency into a quantity called "[semantic entropy](http://arxiv.org/abs/2406.15927)".

So, given an LLM output $$R$$, SeflCheckGPT samples $$n=20$$ extra answers ($$s^1, s^2, ..., s^N$$) from the same LLM (kinda expensive). The formulation here is to measure the "hallucation score" $$S(i)$$ for each sentence $$r_i$$ in $$R$$. SelfCheckGPT sets $$S(i)$$ to be the average distance from $$r_i$$ to each of the sample $$s_j$$:

$$
    S(i) = \frac{1}{N} \sum_n D(r_i, s^n)
$$
, where D is the distance function.

The paper basically lists 4 different variations of $$D$$:
- **Based on BERTScore**: $$D(r_i, s^n) = \max_j B(r_i, s^n_j)$$, where $$B(x, y)$$ gives a similarity score between two pieces of text using the RoBERTa model.
- **Based on a Question-Answering (QA!) experiment**: $$D(r_i, s^n) = \mathbb{E}_{q, \textbf{o}}[\frac{\gamma_2^{N_n}}{\gamma_1^{N_m}+\gamma_2^{N_n}}]$$, where:
  - $$(q, \textbf{o})$$ is a question and set of options generated from $$R$$ (reading comprehension type of questions)
  - $$\gamma_1$$ and $$\gamma_2$$ are hyperparams for smoothening
  - $$N_m$$ are the number of times where the answer of the model based on a sample is the same as that based on a response $$R$$, and $$N_m=N-N_m$$
- **Based on Natural Language Inference (NLI)**: $$D(r_i, s^n) = NLI(r_i, s^n)$$, where NLI is a score given by DeBERTa, an NLI model.
- **Based on another LLM via prompting**: just ask a good LLM like ChatGPT if $$r_i$$ is entailed by $$s^n$$.

Among these four, Prompting has the highest accuracy and also cost. NLI has the best balance betwene accuracy and efficiency, which is the recommended variant for applications.

They also proposed a weird way to approximate white-box method by training an small n-gram based on 21 responses and measuring something from its probability table to measure the hallucination level of the response $$R$$. The unigram variant ended up performed the best among them, probably due to the small sample size.

## Thoughts

![](/assets/fire-fire.png)

*Title of [a Nature article](https://www.nature.com/articles/d41586-024-01641-0) on semantic entropy method*

There has been a lot of skepticism around "using an LLM to check another LLM" type of methods. I understand that and has been following the critical crowd. SelfCheckGPT is actually not perfect yet -- the AUC-PR score of the best variant is just 53% and 67% while we want something like 95%.

However, I see reasons to invest more efforts in this type of method. Humans are not perfect and full of lies. Nevertheless, we have been able to build great civilization out of our hallucinating minds. How did we do that? The answer may be a mix of cooperation, democracy, scientific method, and an appreciation for the truth. As such, there seems to be nothing to prevent a herd of LLMs that democratically and scientifically cooperate to improve itself, just like humans.