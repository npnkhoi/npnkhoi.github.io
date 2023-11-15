---
layout: post
title: Transformer article on Wikipedia
---

This Wikipedia article about transformer is a better read than the original paper as well as the formalization paper. Learnings from this read are:
- Confirmed that [Transformer is not an RNN]({%post_url 2023-08-16-transformer-rnn%})
- Ancestors of the 2017 attention paper is Fast Weight Controller (1992) and a softmax-based attention mechanism (2014).
- For better convergence: A huge model comes with huge risk of bad or lack of convergence. Prominent techniques are learning rate warmup/decay, and layer normalization *before* attention blocks.
- Training objective: Appreciate the unifying framework of T5, which turns all "tasks" (e.g., translation, restoring masks, text classification) into text-to-text, thus reduce the loss function to cross-entropy.
- The 2017 paper has *multiple encoders* and *multiple decoders*.
- For encoders: 
    - The first encoder receives input encodings directly from a lookup table (called embedding matrix), plus a position encodings (which is some just a rollout of a function). 
    - Each encoder is a module that receives encodings for each token, and spits out a matrix with exactly the same shape (representing higher-lever information of the input). 
        - Inside an encoder, the most important component is the *multi-headed attention block*. A single attention block is nice and simple. But for the multi-headed one, is each head produce output with lower dimension so that, when *concatenated*, they form the same dimension again?
- For decoders:
    - The first decoder gets the embeddings of output, masked in a way so that no future information is leaked. (Will do some actual implementation to see it.)
    - Each decoder attention to input from previous decoder (self-attention) or output from an encoder.
        - Wondering: Does the i-th decoder anttend to the i-th encoder's output, of the final encoder's?
    - Finally, the encodings are nicely converted to tokens using a softmax, ready to be punished by the loss function.

Also, still not clear (1) our decoder-only models (like GPT variants) can be useful, (2) a concrete formula from hyperparams (like num heads, embedding dim) to the total number of params.