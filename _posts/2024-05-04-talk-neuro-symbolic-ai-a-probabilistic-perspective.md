---
layout: post
title: 'Talk "Neuro-symbolic AI: A Probabilistic Perspective"'
date: 2024-05-04T01:38:00.000Z
tags: ml ai
---
Attended a talk on neuro-symbolic AI recently. It was by [Kareem Ahmed](https://web.cs.ucla.edu/~ahmedk/) from UCLA, presented at UTD.

I have been fascinated by neuro-symbolic AI for a while. It was first started from [a talk](https://www.notion.so/Neuro-symbolic-AI-A-Probabilistic-Perspective-c034c73077c64d0bb05593dabcf20a6e?pvs=21) I watched in 2021 from some guy at IBM advocating for symbolic AI in current AI. The argument for it still holds over the last three years. From that appreciation, I sometimes get overly excited when I see ideas coming from that realm (such as [AlphaGeometry](https://www.nature.com/articles/s41586-023-06747-5) which claims to be neuro-symbolic — I have not read the report in depth but already feel excited).

![](/assets/uploads/2024-05-01_10-45-59_540.jpeg "An example of a PSL")

The main idea of the talk was to introduce the Probabilistic Semantic Layer (PLS), which is a layer that is supposed to replace softmax in neural networks, that enforces soft constraints that *can represent domain knowledge* to the output of the network. The narrative is as follows:

* As an example, consider a (probabilistic) language model that outputs JSON contents. He says some codeLMs still assign significantly large non-positive weights to syntactically incorrect output. One solution is to somehow reduce the probability for those outputs to near zero.
* The domain knowledge constraints, such as “choosing two in five items such that …”, can be implemented as a “circuit”, which can be translated into a differentiable computational graph to be plugged into a neural network.
* This approach is different from what ChatGPT is possibly doing, which is to first have the core LLM do some inference that may speak inappropriate content, then place a filtering layer on top to review if the content is appropriate. This approach has a drawback, which is that the filtering layer is non-differentiable, making the system not end-to-end trainable.

During the talk, there are some interesting references, such as Perspective API (which takes a piece of content (text?) and outputs the probably that someone might be offended by it) and AutoDiff. Methodologically, I like how he suggests engineering patches, but reason about the soundness in mathematical dimension (KL divergence, first-order Taylor expansion, conditional marginals, etc.)
