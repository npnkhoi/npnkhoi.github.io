---
layout: post
title: The AI Hierarchy
tags: ai
---

![](/assets/deep-learning-book.jpeg)

*The cover photo of the book Deep Learning (Goodfellow, Bengio, Courville)*

I have been noticing that people in my computer science circle do have disparate ideas about the difference between AI, Machine Learning, and Deep Learning. My hierarchy has been AI includes ML, which includes DL. I read it from some book in my undergrad, and I always belive it. Today I read the introduction chapter of Deep Learning by Goodfellow, Bengio, and Courville (2016), and they satisfyingly confirm and extend my understanding. So I will reiterate that hierarchy.

It is: AI > ML > representation learning > deep learning (> transformer)

I have some thoughts on each level of these hierarchy.

AI:
- We are all struggling to define what we mean by AI. In other words, we are trying hard to write a good software requirement specification for the think called AI.
    - The AI textbook of Norvig and Russel gives a four types of AI: [thinking, acting] x [rationally, like humans]. They emphasize "acting rationally" to be the most productive definition.
    - However, I like to think AI is eventually to *follow commands*. Commands can be easy ("how many people are there in this picture?" (attached a pic), "what is the meaning of this meme?") to hard ("bodify yourself into a robot", "make me rich", etc., hack into this bank, etc). Althought most popular "AI" systems today are mostly LLMs, AI in the full sense should be integrated with internet APIs or kinetic hardwares to further emerge into the world.
- Max Tegmark has said in one of his Lex Fridman podcast interview: AI will be dangerous if we (1) connect it to the internet, (2) let it edit itself (program synthesis), and (3) observe human psychology (e.g., tiktok algorithms). We are doing them all, without much limit. It is always dangerous, but I am not sure when would it be uncontrollable even with human coercion.
- The AI course at UT Dallas is mostly, if not entirely, about symbolic AI, which just one approach to AI. Another approach is learning via neural networks (i.e., neural learning?).
    
Machine Learning:
- On the conceptual level, it is very close to what we see in statistics (which is based on probability). Math people like to call it "statistical learning", especially for the simple models. But LLMs seem to be a bit far from the term?
    
Representation learning:
- I just learned today that there is this middle step before becoming to deep learning, and there are other types of representation learning that is not by neural nets.
    
(Skipping deep learning)

Transformer:
- It is currently impressive, but narrow.
- I personally want to see a better learning environment for transformers, namely:
    - More time for them to think and contemplate without judgement: Currently, LLMs during training (pretrain/finetuning) are being judged for every single token that it generate.
    - More lively environment such as in (self-?)reinforcement learning: This may require either a very good simulation, or turning AI into an self-sustaining agent in the world.
