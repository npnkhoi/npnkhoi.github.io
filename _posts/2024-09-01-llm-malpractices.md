---
layout: post
title: Malpractices in LLM research
tags: ml
---

https://aclanthology.org/2024.eacl-long.5.pdf

This paper, published in EACL 2024, argues that evaluation results of close-sourced models like GPT4 are severely unreliable, done via malpractices. Those malpractices include:
- Data contamination: Leaking the test set to the model itself (via the use of ChatGPT web interface that seems to allow learning from the user prompts)
- Reproducibility issues: 
  - Only half of the papers examined (212) provided code repository. Funnily and sadly, some papers provide link to an empty or invalid repository... (Why do you do that, researchers?)
- Evaluation fairness issues:
  - ChatGPT is usually thought to be the only model that should be measured. Many papers don't bother to compare ChatGPT's performance to other models.
  - No statistic tests are performed on the performance results of the models
  - Different samples used between closed-sourced and open-sourced models are done in an unfair way

To protect the integrity of NLP research, report indirect data leakage at https://leak-llm.github.io/.