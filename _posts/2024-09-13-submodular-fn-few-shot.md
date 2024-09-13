---
layout: post
title: "Submodular Functions for Few-shot Learning"
tags: ml
---

A big question in few-shot learning, especially when you have a sizeable set of labelel data, is how to select the most "informative" set of demonstrations to put in the prompt.

An [NAACL 2024 Findings paper](https://aclanthology.org/2024.findings-naacl.209) (and related research) is proposing a very nice solution that is based on an intuitive optimization objective. The use case is as follows: you have a large set of _unlabeled_ inputs $$V$$. To do few-shot learning, you probably need to do two things: (1) hand-annotate a fixed subset of inputs $$A$$, and (2) during inference time, select a subset of $$A$$ to set as demonstrations in the prompt.

![](/assets/facility-location.png)

*What is this figure about? Facility Location problem or Demonstration Selection problem? We have no idea! And that's the great idea of this paper.*

The paper key idea is to solve the two problems separately, but in the same way: optimizing the selection of examples as solving Facility Location problem. This problem is, given a matrix of distances (or similarities) between objects, choose a few objects to minimize the sum of min distances to all other objects. Here, distances to Facility Location problem is as semantic similarity score (e.g., BERTScore) between examples. Now our job is just to apply off-the-shelf solvers for Facility Location to select the most informative examples. Nailed it!

I am excited to look for ready-to-use packages that implement this idea to apply to my few-shot learning experiments.