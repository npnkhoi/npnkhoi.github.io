---
layout: post
title: Reproducibility in Science
tags: science
---

The topic of scientific misconduct has been popping up quite a bit in my life. 

For example, I recently listen to [this Vox podcast](https://pca.st/roovwtgm) about a Stanford (or Harvard?) professor being accused of faking experimental data. Furthermore, it raises a warning about the motive system in academia, where there are so much benefit in faking research data, while the risks don't seem to be as much. 

Meanwile, a post in a private Vietnamese PhD community on Facebook brought up the issue of reproducibility in machine learning research. In particular, they tried to replicate the results of a "state-of-the-art" paper, but the results are noisy and don't seem to be statistically better than the previous state-of-the-art. That reminds me about the way people report AI models' performance in Machine Learning papers. They don't seem to care about the fact that the performance measures are random variables, and they need a sufficiently large sample to really make some statistical claim about the performance.

Without much insider knowledge, I am very curious (and a bit concerned) about how integrity is being maintained in the Machine Learning research community today. The motivation to fabricate data is too much because authors are under huge pressure to produce publications. And the "vomit" of ML publications these days makes me ask myself: how to audit these results? 

One place to start is the experimental design. The experimental design of ML experiments are precisely described in their code. However, there are two problems with the code: (1) sometimes they are not public, and (2) they are usually too complicated to comprehend. One rule of thumb I learned while doing research is that "if your code returns good results, your code is bug-free". This rule is funny, wrong, and should make you feel very concerning about the integrity of those code.

Next questions: who are auditing these results? *Volunteer* reviewers. This is one of my biggest surprise when I learned about academia. These reviewers are of course credible people, ranging from high-profile researchers to first time authors like me currently. However, they are not paid for their reviews. On the other hand, reviewing such papers are very time-consuming. So I feel like the reviewers are really just volunteering, and the quality of reviews can *silently* be low. Given these reviews are the ultimate source of truth for publication acceptance, which decides success of researchers, which decides their admission to positions in academia, which decides the training of the next generation of researchers, I do think there should be a way to improve the motive system of conference reviewing. Or we will see whole AI bubble explodes before starting.

Dear readers: What are your thoughts about the review system in science? Is it actually that bad? If so, how to improve it?