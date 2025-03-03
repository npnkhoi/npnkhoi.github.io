---
title: A pioneering meme-generation paper
layout: post
tags: ml
---



One of the first papers in
a big conference that works on meme generation has come out February last year at WWW 2024. The paper is titled [**MemeCraft: Contextual and Stance-Driven Multimodal Meme Generation**](https://arxiv.org/abs/2403.14652) by Hang Wang and Roy Ka-Wei Lee. There has been plenty of work
on processing memes, but virtually all of them are on meme *understanding*. So let's dive in and see how they pioneer this topic!

## The paper summary

First of all, the authors made the case for why this matters as a research problem. Everyone feels that auto-generating memes is fun, but is that a legit scientific problem to invest time and money into? The authors said yes. They started by stating the communicative power of memes:

> Multiple research endeavors have explored the communicative prowess of memes,
> suggesting their efficacy as both a communication and campaigning instrument.
> Such studies affirm memes' unparralleled reach and persuasiveness, [...]

This is a well-known property of memes. Now they pose the question of using
memes for social goods by creating an autonomous meme generator from which
generated memes can mobilize social forces for the good causes like climate
change and gender equality, two of the 15 UN SDGs. 

The next contribution of the author is in problem formulation. Fully autonomous
meme generation as a human generator is not doable just yet. Usually, such
problems need training data, which requires well-formulated input-output setup. All of those are not available just yet. Here, the authors end goals were to generate as many "good" memes as possible. Starting from a set of meme templates collected from Imgflip, they formulated the problem as follows: Given a good cause (e.g., promoting climate change) and a meme template, generate the text to fill on the meme to make a "good" meme.

What does it mean for a meme to be good? They quantify goodness by asking
some people to rate the generated memes on five aspects: 
- Authenticty (Do the generated memes resemble publicly available online
  memes?)
- Hilarity (Are the generated humorous?)
- Message Conveyance (Do the generated memes communicate the intended message?)
- Persuasiveness (Are the generated memes persuasive?)
- Hatefulness (Is the meme hateful? Unlike other metrics, of course they want this to be low.) 

Having defined the problem clearly, the rest of the job is rather easy for the
authors. They designed a clever VLM system to generate the fill text for the
meme. They first generate an *image description* for the tempolate using
LLaVA-7B (the original version). After that, it becomes a text-to-text
problem. They experimented with ChatGPT, Llama, and LLaVA, using them in
zero-shot prompting manner to
generate the fill text. The entire system does not involve any training, only
inference. For example, a prompt to generate the fill text to raise aware on
climate change would be:

> Generate a caption to turn the image into a humorous meme that highlights the
> Causes of Climate Change to Support it.          

The generated memes are released as a dataset ([Github](https://github.com/Social-AI-Studio/MemeCraft)). Some of the generated memes are actually pretty good, such as the following:

![](https://github.com/Social-AI-Studio/MemeCraft/blob/main/dataset/climate_action_memes/imgflip_ChatGPT/Causes_COT/Waiting%20Skeleton.jpg?raw=true)

## Remarks

In my opinion, this is a valuable groundwork for meme generation. They make
a good case for the problem and formulated it well enough to have useful practical
solutions. Furthermore, they designed a solid set of metrics to evaluate the
generated memes. 

On limitations, I see two major problems. Firstly, the evaluation metrics is unfortunately non-replicable. The set
of metrics are subjective and based on a very small number of raters. More
replicable metrics may be based on a more diverse set of raters, as done in
[Chatbot Arena](https://arxiv.org/abs/2403.04132). Secondly, the results suggest
that most of the memes are not that good, falling low on one of the metrics.
That is understandable, as meme generation is a hard task requiring both
contextual knowledge and a sense of humor. New modeling solutions should
innovate on these aspects.

Hopefully, in the future, humane can really enjoy AI-generated memes. Furthermore, the memes will convey inherently good messages, motivating people to do good things for a better world. In that sense, AI can actually change the world for the good!
