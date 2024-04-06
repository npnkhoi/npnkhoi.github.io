---
layout: post
title: Quiet-STaR
date: 2024-04-06T08:54:00.000Z
tags: ml
---
A new [preprint](http://arxiv.org/abs/2403.09629) from Stanford, arxiv-ed 3 weeks ago entitled "Quiet-STaR: Language Models Can Teach Themselves to Think Before Speaking". The main goal is to efficiently allocate more time for LLMs when generating hard tokens, such that the next token in "12+54=". This problem has a flavor of planning (the next token to be generated has an effect on the ultimate quality of the entire generated text), search (among many next possible tokens, which one should be chosen?), and reward (e.g., when doing unsupervised language modeling, being able to generate the original text is the objective). I like this line of research, as it allows LLM to have a [scratchpad](<{%post_url 2024-01-21-chain-of-thought%}>) to cook before generating serious text to be evaluated. (Only 1984 Big Brother would penalize a thought!)

![](/assets/uploads/screenshot-2024-04-06-at-8.57.50 am.png "Algorithm illustration")

^ General overview

The main algorithm here is pretty complicated (Algorithm 1). I only understand that the algorithm allows a lot of thinking time for every single token being generated. In the image above, I highlight in red the symbols that I am not sure about the semantics. For example, how do we assign a value to a function ($$log p^init_...$$)? What is the shape of tensor $$T_j$? What is the qualitative difference between the REINFORCE loss and the NLL (negative log-likelihood?) loss?



![](/assets/uploads/screenshot-2024-04-06-at-2.15.45 pm.png)

But I love the fact that a formal algorithm is presented here so that people who are capable can precisely understand and critique the algorithm.

This article also shows me some new techniques, such as meta-token learning (like a magic word that triggers nice behaviors in LLMs), avoiding distribution shift in finetuning LLMs by a shallow mixture FFNN, the mask matrix being used to achieve parallelism (Figure 3), real techniques in avoiding overfitting, etc.

In terms of results, I realized a variant of GPT-4 has already nearly [perfect results](https://paperswithcode.com/sota/arithmetic-reasoning-on-gsm8k) on GS8MK (97%), which is the benchmark on which Quiet-STaR was tested. But perhaps if GPT-4 is equipped with Quiet-STaR, performance will improve for harder tasks?
