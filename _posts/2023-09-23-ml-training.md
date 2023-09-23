---
layout: post
title: An Average Machine Learning Practitioner
---

TLDR: I show two cool ML tricks. 'Grid search' is a wrong name. And I am average in training ML models.

## Some ML tricks

Today, I am happy to learn some cool ML knowledge about inspecting a ML model. Classically, we look at the training curves, where you plot the performance (in accuracy or loss) of your model against training time (e.g., num epochs), on both the training and validation set. That helps with balancing over- and under-fitting. But with simpler[^1] models like a Linear Regressor, you can do more useful tricks to *listen to* what the model is actually telling you about the data. 

[^1]: I wanted to use more precise words like 'interpretable' or 'transparent', but I honestly don't know what is the correct word.

The first trick to observe the values of each parameter over training time. In simple models, we probably know the meaning of each param. Like in linear regression, the coefficients are the level of linear correlation[^2]. So by looking at the changes of these params, you know how the model (or, pardon me, 'the AI'), to change its mind about the data and the world. Subsequently, the convergence of these params would mean the model has almost nothing to gain from the data, and we should halt the training loop.

[^2]: I may be wrong. People have methods to measure linear correlation -- either Pearson or Spearman coefficient. Not sure if the coef of a linear regressor is equivalent/related to those.

The second trick is plotting the 'hyper plane slice'. Given my little understanding of this trick, I know that this allows me to see how accurate the model is thinking about the data via the lens of only one (or a few) parameters. More on that in later posts.

## Thoughts about Grid Search
I have a mysterious hatred with this technique. Oftentimes in the past, when I ran grid-search, it takes more than a minute to finish. And there I was not in the mood to wait because I was probably using a Google Colab, which requires painful tricks to keep the interface awake. And the hassle to save the model ASAP after the search is done (so that I don't lose the hard-earned model) is stressful.

Also, I feel like the word search is not suitable for this technique. Search is a while loop that we truly don't know when it will stop. Grid search is a fixed-time for loop. 

Firstly, let's acknowledge that this technique belongs to the family of [hyperparameter optimization](https://en.wikipedia.org/wiki/Hyperparameter_optimization)[^3] techniques. Even this name is not good for me because optimization sounds pretty rapid, but this is a slow thing. But that's okay.

[^3]: On a small tangent, let's mention [Optuna](https://optuna.org/) as an emergingly famous tool to do hyperparam optimization. I will learn about it one day.

Sklearn called it [exhaustive grid search](https://scikit-learn.org/stable/modules/grid_search.html#exhaustive-grid-search), which is just slightly better -- the 'search is still there'. Therefore, I would like to propose a better name -- **grid exploration**. You explore uniformly all settings in the grid, and *report back* all the samples you collected at those settings. Like the Mar Rovers. That makes me want to implement it so much, makes me feel like a NASA programmer.

## "Optimizing accuracy"
As usual, I take this chance to think a bit more broadly. And I realized I had been constantly surprised by how inexperienced I am compared to my undergrad friends in optimizing for accuracy in ML. Somehow, a lot of them are very pragmatic and could achieve really high results on unseen data. I was in a Machine Learning class where my ranking is right at the middle, which means my ML engineering skill is around the average.

But that should not be surprising. Training a ML model is a dark art. It a place where [good execution is needed more than good ideas]({%post_url 2023-09-19-educator%}). There is so many tricks you can do to achieve a good score, and most of the tricks are based on the so-called experiences and intuitions. It is probably not a skill where you can take shortcuts by being a good mathematician, rationalizing the problem, predicting that technique would work without actually running experiments. Unfortunately, that is the mindset I am unembarassedly embracing.

## From Here

Anyway, there will come a time when I need to do a grid exploration on how to train an ML model. I am both excited and lazy to see it coming. Is Kaggle a good place to start?