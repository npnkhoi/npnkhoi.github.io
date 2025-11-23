---
title: Matrix decomposition
tags: math
layout: post
---

_Disclaimer: Nov 23, 2025: After re-reading this post, I saw several conceptual errors and typos. I will try to fix them, but please do not take what I write here as the source of truth. I recommend reading Linear Algebra textbooks._

I recently realized why linear algebra is called linear algebra. It starts from the word *algebra*, which is the study of abstract systems and the manipulation of expressions within those systems. In *linear algebra*, that abstract system contains vectors, matrices, and tensors. So it studies how to manipulate matrix expressions. For example, it allows us to replace the expression $A^{-1}$ by $A^T$ when $A$ is an orthonormal matrix. 

Such manipulations can lead to powerful results and applications. In this post, let’s visit one of those powerful things: the problem of **matrix decomposition**. The objective of this problem is to express an input matrix $M$ as a product of two or three “special” matrices. This decomposition in itself is perhaps not yet useful. However, it enables important downstream tasks, especially in pattern recognition and data compression. For example, Principle Component Analysis is a technique for compressing data, visualizing high-dimensional data (by compressing to 2D or 3D), and extracting linear features, among many other usages. At the same time, PCA is directly based on the Eigen Value Decomposition technique.

A few prominent decomposition methods are Singular Value Decomposition, Eigen Value Decomposition, Q-R decomposition. I only had a chance to review the first two, so let only visit them :D

## Singular Value Decomposition

In SVD, given $M\in\mathbb{R}^{m\times n}$, it finds three matrices $U, \Sigma, T$ such that:

1. $M=U\Sigma V^T$
2. $U,V$ are orthonormal (i.e., a matrix whose columns vectors have norm of 1 and are pair-wise orthogonal).
3. $\Sigma$ is a diagonal matrices, i.e., a square matrix where only the item on the main diagonal (coordiates [i, i]) are non-zero.

What are the sizes of those decomposed matrices? That is actually a hyper-parameter decided based on applications. Note that if we know the number of rows of $\Sigma$, we will know the size of all three matrices. There are four main versions of $M$’s size:

- **Full version**: $\Sigma$ has $max(m, n)$ rows.
- **Thin version:** $\Sigma$ has $min(m, n)$ rows.
- **Compact version**: $\Sigma$ has $rank(M)$ rows. This is probably the most compact version to do lossless SVD.
- **Truncated version**: $\Sigma$ has $t<<rank(M)$ rows. It is used when $M$’s rank is still too large and there is not enough space to store the compact version.

That is all I could gather for now. Some further questions to review is:

- What is the canonical method to do SVD?
- Given that the values on the diagonal of $\Sigma$ is called the singular values, what are their meanings and why?

## Eigen Value Decomposition

### Definition

To understand EVD, we need the concept of diagonalization. A matrix $M$ is diagonalizable $\Leftrightarrow$  $\exists$ a reversible matrix $P$ and a diagonal matrix $D$: $M=PDP^{-1}$.

In EVD, given a diagonalizable matrix $M\in\mathbb{R}^{n\times n}$, it finds two matrices $V,D\in\mathbb{R}^{n\times n}$ such that: $M=VDV^T$.

### Decomposition method

It can be proven that:

1. A diagonalizable matrix of size $n\times n$ has $n$ linearly independent eigenvectors [1; Theorem 5.2.1]
2. (From 1 and EVD definition) In the EVD $M=VDV^T$, $D$ contains all of $M$’s eigenvalues on the diagonals, and the eigenvectors are the corresponding column vectors in $V$.

What are eigenvalues and eigenvectors again? Given a matrix $M\in \mathbb{R}^{n\times n}$, a scalar $\lambda$ is an eigenvalue of $M$ $\Leftrightarrow \exists$ a non-zero vector $x\in\mathbb{R}^n$: 

$Mx = \lambda x$. (1)

That vector $x$ is called the eigenvalue corresponding to $\lambda$.

Theorem 2 shows a way to perform EVD, which is to compute all the eigenvalues and eigenvectors of $M$. How? Solve for $\lambda,x$ in Equation (1). They are the solution of the “characteristic equation” of $M$ (equivalent to (1)): $(M-I\lambda)x=0$. To solve this, notice that $x$ has to be a non-trivial solution, which implies $det(M-Ix)=0$. That gives a polynomial equation with one unknown $\lambda$, which is now solvable.

## EVD’s application: Principle Component Analysis

PCA is probably too famous to warrant a motivation. Given a matrix $M\in\mathbb{R}^{m\times n}$ and a small number $k$ (2 or 3 for visualization), it finds two matrices $A$ and $V$ such that:

1. $A\in\mathbb{R}^{k\times n}$
2. $V\in\mathbb{R}^{k\times m}$
3. $M\approx V^{T}B$

The approximation error is quantified by the Frobenius norm of the difference between two sides. (Frobenius norm of a matrix = sum of L2-norms of all its columns.)

And guess what? The analytical solution to PCA is actually obtainable via EVD as follows:

1. Let $X=MM^T$
2. Run SVD: $X=U\Sigma Z^T$.
3. $V$ (of PCA) is the transpose of the k most dominant eigenvectors in $U$.

As mentioned earlier, PCA has many applications. It can be used to project high-dimensional data into 2-3D in such a way that keep the most variance in the data. It can also be used to compress data: notice how $M$ of size $m\times n$ is know approximated by two matrices of total size $k(m+n)$. This low-rank approximation is the very premise of low-rank adaptation, an model fine-tuning technique that allows training only 0.5% the size of an LLM while still effectively updating its behavior.

## Another application: Multi Dimensional Scaling

For this problem, I am only presenting the problem and state that it is solved by decomposition. The problem is as follows: given $D\in\mathbb{R}^{n\times n}$ supposedly being the distance matrix between $n$ $k$-dimensional vectors. Find those vectors.

There is an efficient algorithm to determine a set of vectors that give the exact same distance matrix. The algorithm is to do EVD on the “Gram matrix” of $D$.

This is quite related to two things in modern machine learning. Firstly, MDS is an instance of embedding, which is the general problem to turn high-dimensional data to low-dimensional one. Secondly, when only a sample of entries in $D$ is available and those are binarized (into 0s and 1s), this is similar (but not the same!) with contrastive learning.

## References

[1] howard-anton-chris-rorres-elementary-linear-algebra-applications-version-11th-edition

[2] Haim Schweitzer’s Data Representation lectures, which is from his course that I am taking this semester
