---
title: An interesting solution to a classic pumping-lemma problem
layout: post
tags: cs
---

There is a nice problem about proving non-regularity of a language using pumping lemma. The nice thing is not the problem itself, but the existence of a nice solution for it. 

## Reviewing Pumping Lemma

First, let review the pumping lemma. It is a theorem in computing theory, stated as follows:

> If a language $$L$$ is regular, there exists an integer $$p$$ (called the pumping length) such that:
> - for all string $$s \in L$$ that is longer than $p$, $$s$$ can be partitioned into three parts $$\overline{xyz}=s$$ such that:
>     - $\| xy \| \leq p$
>     - $\| y \| > 0$
>     - $$\overline{xy^iz} \in L$$ for all $$i$$

The theorem can also be stated in first order logic style:

> $$L\in REG \rightarrow \forall s \in L \land \| s \| > p \rightarrow \exists x \exists y \exists z ((s=\overline{xyz}) \land (\left| xy \right| \leq p) \land (\left| y \right| > 0) \land (\forall i \; \overline{xy^iz} \in L))$$

**Sketch proof.** If $L$ is regular, there exists a deterministic finite automaton that decides it. Let $p$ be the number of states of this DFA, which is finite. If a string $s$ with length larger than $p$ is in $L$, $s$ must cause a *loop* in the DFA. From there, we can (1) characterize the substring that causes the loop and (2) be sure that removing or duplicating the substring will results in new strings that must also be in $L$.


## A problem with two nice solutions

**Problem.** Proving non-regularity of the non-palindrome language, i.e., $$L = \{w \in \{0,1\}^* \mid w \textbf{ is not a palindrome}\}$$

As pumping lemma is the "canonical" method for proving non-regularity, one might attempt to apply it to this problem. But it will turn out that naively picking some string in $L$ (such as $0^p10^{p+1}$) makes it impossible to apply the pumping lemma.

**Approach 1.**The simpler approach is to prove the non-regularity of the complement language $\bar{L}$, which is the set of all palindromes. First, assume $\bar{L}$ is regular. Then, choosing the string $0^p10^p \in \bar{L}$ and pumping it up will leads to contradiction. Finally, due to the closure under complement of regular language, 

However, is it actually impossible to use pumping lemma directly on $L$? Do we have to be creative and think of the complement language in order to prove this theorem? It turns out, we don't have to! There is a nice proof that directly uses pumping lemma on $L$. The key is in choosing the initial string for pumping. Here's the proof:

**Approach 2.** Assume $L$ is regular with pumping length $p$. Let $s = 0^p10^{p+p!}$. We can see that $s \in L$ and is longer than $p$. Decompose $s$ into $\overline{xyz}$, we know that $y$ contains only 0's and belong to the "left" part of $s$. We will pump $y$ to $1+\frac{p!}{\|y\|}$ times. Because $\|y\|$ is an integer no larger than $p$, $\frac{p!}{\|y\|}$ is a natural number, making the pump valid. Furthermore, the pump results in a palindrome, which is not in $L$, causing a contradiction.

This is such a beautifully creative solution to me. Whoever can think of this solution needs to be stubborn enough to stick with pumping a string in $L$, while also sharp enough to recognize the failture of naive selection of $s$ to choose a new $s$ that guarantees successful pumping.


## Broader thoughts

Reading about pumping lemma makes me think about soundness and completeness properties in logic theory. They are properties of inference rules. A sound rule is a rule that always produces logically correct statements. A complete set of a rules are one that can prove anything that is correct (i.e., consistent with the knowledge base). Because pumping lemma is a theorem about regular languages, we know for sure that it is *sound*. But is it *complete*, i.e., pumping lemma can be used to prove non-regularity of any non-regular language?

A tangent thought is about the application of regular languages in NLP. Even though modern NLP is full of LLM vomit, Jurasky and Martin's [SLP2](https://web.stanford.edu/~jurafsky/slp3/2.pdf) textbook mentions regular languages as a tool for pre-2010 NLP, such as in word tokenization. It was perhaps a cute period in NLP history where the canonical methods are very sound with a lot of theoretical understanding around them, but they are not very useful for real-world applications.
