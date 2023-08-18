---
title: Transformer is not an RNN?
layout: post
---

I am reading about the fundamentals related to Transformers, starting with the arxiv paper from DeepMind last year -- _Formal Algorithms for Transformers_ [1] -- and connecting that with the knowledge about previous models -- RNN and LSTM. A surprise I found: While an LSTM is a RNN, a Transformer is not. RNN and Transformer are different in (surprisingly) several ways:
- RNN takes unlimited-length input, while Transformer takes a fixed length input.
    - RNN does that by keeping a "state vector/matrix" that remembers information about the arbitrariy long list of preceding tokens.
    - Transformer, on the other hand, fixes the number of "input" to be a certain number, like 786 or 1024. ChatGPT's length is about a few tens of thousand max.
- RNN returns a vector (or matrix) about the whole sentence (and further do prediction with that vector), while Transformer generates a vector (contextualized, or dynamic, embeddings!) for each token.
    - RNN: with "that vector", an trivial thing to do is sentence classification. But a more surprising (but in fact pretty trivial) task is next-token prediction by the virtue of _classifying_ which token is the best token to be next.
    - Transformer: This is more general than the mechanism of RNN. In a past project with transformer, I was wondering about the characteristics of the dynamic embeddings that models like Tranformers generate. In particular, what would the geometry of the generated embeddings tell something about the meaning of each word already? What are the differences with that dynamic embeddings with the static of Word2Vec [2]?

On a quick note, LSTM (based on my reading so far) is just a better subset of RNN that resolves the vanishing and exploding gradients problem. The [video by StatQuest](https://www.youtube.com/watch?v=YCzL96nL7j0) explains it the best.

**References**

[1] Mary Phuong and Marcus Hutter, “Formal Algorithms for Transformers” (arXiv, July 19, 2022), https://doi.org/10.48550/arXiv.2207.09238.

[2] Tomas Mikolov et al., “Efficient Estimation of Word Representations in Vector Space,” ArXiv:1301.3781 [Cs], September 6, 2013, http://arxiv.org/abs/1301.3781.