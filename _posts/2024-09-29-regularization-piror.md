---
title: Regularizations as priors
tags: ml
layout: post
---

Regularization is a common technique to prevent overfitting in machine learning models. It adds a penalty term to the loss function to discourage the model from fitting the training data too closely. But at a Bayesian statistics [summer school]({% post_url 2023-07-23-bayesian %}), I heard a different perspective on this: regularization can be seen as a "prior" on the parameters. If this is true, then we can appreciate the theoretical justification for regularization. So, how come regularization can be seen as a prior?

As of now, I can see this equivalence holds for simple models, like logistic regression with L1 and L2 regularization prior or Naive Bayes with Laplacian smoothing.

For Logistic regression, recall the model to be:

$$
    P_{\textbf{w}}(y = 1 \mid \textbf{x}) = \sigma(\textbf{w}^T \textbf{x})
$$

Now, we apply Bayes rule to learn the best parameters $$\textbf{w}$$ for this model. Best parameters mean the ones that maximize the posterior probability. Based on the Bayes rule, the prosterior is proportional to the likelihood times the prior. Note that the "model" here must be the "model expression" of the current model.

$$
    P(\textbf{w} \mid D) = P(\textbf{w} \mid X, \textbf{y}) \propto P(\textbf{y} \mid X, \textbf{w}) P(\textbf{w})
$$

where $$D$$ is the training data. When we take the negative log likelihood of the posterior, it becomes our loss function:

$$
    \text{loss} = - \log P(\textbf{w} \mid D) = -\log P(\textbf{y} \mid X, \textbf{w}) - \log P(\textbf{w})
$$

Notice the second term. It is the negative log likelihood of the prior. If we put a Gaussian prior over $$\textbf{w}$$:

$$
    P(\textbf{w}) = \frac{1}{\sqrt{2\pi\sigma^2}^d} \exp\left(-\frac{\|\textbf{w}\|^2}{2\sigma^2}\right)
$$

, the second term becomes the L2 regularization term:

$$
    - \log P(\textbf{w}) = \frac{\lambda}{2}\|\textbf{w}\|^2
$$

where $$\lambda$$ is the regularization parameter.

Similarly, if we put a Laplacian prior over $$\textbf{w}$$, the second term becomes the L1 regularization term:

$$
    - \log P(\textbf{w}) = \lambda \|\textbf{w}\|_1
$$

This is a wow moment for me. I never realized regularization has such a nice interpretation. It is not just a heuristic. It is a prior being applied via Bayes rule!

Now for naive Bayes, a similar story holds. There, people usually use k-laplacian smoothing. What is k-laplacian smoothing? It is equivalent to putting, guess what, a prior over the parameters of the Naive Bayes model!

That's it. For more complex models, like a neural network, I am not sure if this formalization still holds. But at least for now, I find this perspective very satisfying for simple models.

