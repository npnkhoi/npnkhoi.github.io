---
layout: post
title: Theory of Computation Review
tags: cs
---
*This is a midterm review for CS6382 ([syllabus](https://personal.utdallas.edu/~dxd056000/cs6382.html))*

## Important problems

### Topic 1: Determining decidability

#### Concepts
- r.e. = Turing-recognizable
- recursive = Turing-decidable
- A r.e. property $$A$$ is a language of *TM codes* such that every pair of TMs that generated the same language must either both inside or outside of $$A$$

#### Halting problem $$\langle x, M \rangle$$, but fix $$x$$. Is this decidable?

#### Halting problem $$\langle x, M \rangle$$, but fix $$M$$. Is this decidable?

### Topic 2: "Characterization" of NP
Informally, the NP class is defined as the collection of languages that can be recognized by a Non-deterministic Turing Machine (NTM) in polynomial time.

To precisely define "polynomial time", and "can be recognized", we come to the following definition. $$A \in NP \Leftrightarrow \exists B \in P, \text{polynomial } p: \forall x, \vert x\vert = n, x \in A \Leftrightarrow (\exists y, \vert y\vert \leq p(n))[\langle x, y\rangle \in B]$$

Human language: $$A$$ is a language in NP if and only if 
- there eixsts 
    - another language $$B$$ in $$P$$
    - a polynomial $$p$$
- such that: 
    - for any string $$x$$ with length $$n$$: 
        - $$x$$ belongs to $$A$$ if and only if:
            - there exits a string $$y$$
            - such that:
                - length of $$y$$ does not exceed $$p(n)$$
                - the concatenation $$\langle x, y\rangle$$ belongs to $$B$$.

With that, $$p()$$ and the fact that $$B \in P$$ formalizes the notion of polynomial time. The running of the NTM is translated to the existence of a polynomial length string $$y$$ (representing the running path of the NTM). $$y$$ and the language $$B$$ is the representation of the NTM.

In some cases, we restrict the alphabet for $$y$$ to be $$\{0, 1\}$$.

### Topic 3: Using Partition and Subsum to prove NP-completeness

#### Concepts
The following two problems are NP-complete:
- **Partition**: Given a set of positive intergers $$A$$. Check if there exists a partition $$A_1 \cap A_2 = 2$$ (disjoint) such that Sum($$A_1$$) = Sum($$A_2$$).
- **Subsum**: Given a set of positive intergers $$A$$. Check if there exists a subset $$B \subset A$$ such that Sum($$A$$) = $$S$$.

To prove a problem $$A$$ is NP-hard, we "reduce" an NP-hard problem $$B$$ to $$A$$. May have to turn $$A$$ to a decision version. Depending on the reduction specified, we have a corresponding method:
- If using many-to-one reduction, we need to (1)construct a polynomial-time many-to-one reduction algorithm to reduce the input $$y$$ of $$B$$ to the input $$x$$ of $$A$$, then prove that (2) $$y \in B \Rightarrow x \in A$$ and (3) the converse.
- If using Turing reduction, we need to construct a polynomial-time DTM with oracle A that accepts B.

### Topic 4: Using Turing-reduction to prove a completeness in Polynomial Hierarchy

#### Concepts
- More about Turing reduction:
    - rather than changing the input to another one in many-one reduction, we use the original input, but consulting an oracle in the TM.
    - It is transitive.
    - Notations for $$A \leq^p_T B$$
        - $$A \in P(B)$$,
        - or $$A \in P^B$$.
    - It is a "weaker" reduction than many-to-one.
    - It should not be merged naively with many-to-one.
- Polynomial Hierarchy (PH) arises from this:
    - The hierachy starts with $$\Sigma^p_{0} = \Pi^p_{0} = \Delta^p_{0} = P$$
    - Then built by: $$\Sigma^p_{n+1} = P(\Sigma^p_n), \Pi^p_{n+1} = NP
    (\Sigma^p_n), \Delta^p_{n+1} = co-NP(\Sigma^p_n)$$
        - Level 1: $$\Sigma^p_1 = NP(P) = NP; \Delta^p_1 = co-NP(P) = co-NP(P); \Pi^p_1 = P(P) = P$$
        - Level 2: $$\Delta^p_2 = P(NP)$$ ...
    - Finally, $$PH = \cup_n \Sigma^p_n$$

#### Example: Prove that Exact-Clique is $$\leq^p_T$$-complete in $$\Delta^p_2$$
Proof:
- We have Exact-Clique $$\leq^p_T$$ Clique $$\Rightarrow$$ Exact-Clique $$\in P(NP) = \Delta^p_2$$
- Every problem in $$\Delta^p_2$$ can be Turing-reduced to some problem in $$NP$$, which can be many-one-reduced to Clique, which can be Turing-reduced to Exact-Clique (q.e.d.)


### Topic 5: Proving Space Bounded Halting Problem is PSPACE-complete
**Problem.** SBHP = "Given an DTM M, an input x and a string $$0^s$$, can M accept x using space at most s?" Prove that SBHP is PSPACE-complete by many-one reduction.

**Proof.**
- Language form: $$L=\{\langle m,x,0^s \rangle \vert M \text{ accepts } x \text{ within space } s\}$$
- First, prove it belongs to PSPACE by the existence of the universal TM.
- p-m reduction: From a string y in A, construct the input $$\langle M, y, 0^{p(\vert y\vert)} \rangle$$ for $$L$$. We have $$A\in PSPACE \Leftrightarrow \langle M, y, o^{p(\vert y\vert)} \rangle \in L$$. Therefore, we have reduced all problem in PSPACE to $$L$$.


## Miscelaneous
### "The barber that cuts his own hair"
- Diagionalization technique is very intersting. Used to prove something is non-countable by contradiction.
- Halting problem is one of those. The language version: $$\{M \vert M \text{ accepts } code(M)\}$$
    - Method 1: See the textbook
    - Method 2: Still cooking it ...
    - In class, my prof used the [barber paradox](https://en.wikipedia.org/wiki/Barber_paradox) to illustrate. I was in fact inspired by this technique to [cut my actual hair]({%post_url 2023-10-06-self-hair-cut%}).