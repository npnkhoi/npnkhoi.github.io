---
layout: post
title: Thinking about scratchpads
tags: cs ai
---


This blog post is about chain of thought, and how to make LLMs smarter. 90% are well-known ideas, while the rest are speculations and hypotheses that may already been tested by someone who already submitted a manuscript about those very ideas.

We start with the question: **where is the thinking time, or scratchpad, for LLMs?**

- This problem is *very* SOTA. In a recent podcast interview with Bill Gates (very likely in Jan 2024), Sam Altman also admitted this problem to be one of those to be solved to make LLMs smarter. Even OpenAI is still working on as we speak.
- Nye et al [1], in the context of program synthesis, finetuned to generate correct **scratchpad** and answer. 
	- This is one of the first efforts in giving scratchpad to LLMs.
	- They do specify in the future work section that efforts should be made to enable learning to use scratchpad **without direct supervision** (which I am intersted in). To extend that idea, I think we should modify our objective function/training algorithm so that only wrong **answers** are penalized, and **scratchpad is ignored**. That may require breaking certain conventions in ML training loops. But let's see. To learn effectively, humans may need to think slowly!
- The CoT paper [2]: They just formalize the notion of reasoning steps from [1], but only introduced it for **prompting** methods? That means you can only choose either large training set, or chain-of-thought, not both. That should not be the case!
	- I know that pretrained models are often expected to be the last artifact of large-scale training. However, even human "experts" do have to learn for months to acquire new skills. It is impossible to expect LLMs to be trained once and for all.
- A Korean author group posted on CoT finetuning in October 2023 (3 months ago) [3]. But their selling point is (just) that it helps small models perform better. ALso, they still follow the same method as Nye et al I belive.
- My proposal: Finetune LLMs on large amount of data where only the answers are available for each example, while the reasoning steps are hard to collect. During training, don't penalize the scratch pad.

## References

[1] M. Nye et al., “Show Your Work: Scratchpads for Intermediate Computation with Language Models.” arXiv, Nov. 30, 2021. Accessed: Jan. 21, 2024. [Online]. Available: http://arxiv.org/abs/2112.00114

[2] J. Wei et al., “Chain-of-Thought Prompting Elicits Reasoning in Large Language Models”.

[3] S. Kim et al., “The CoT Collection: Improving Zero-shot and Few-shot Learning of Language Models via Chain-of-Thought Fine-Tuning.” arXiv, Oct. 14, 2023. Accessed: Jan. 21, 2024. [Online]. Available: http://arxiv.org/abs/2305.14045
