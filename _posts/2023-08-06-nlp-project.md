---
title: "Text matching in pharmacy: A Summer NLP project (part 1)"
layout: post
---

<!-- TODO: Abstract?  -->

## Introduction
- invited by a friend to work for their team on data analytics (freelance, one month). The motivations were to (1) practice NLP, (2) fill in my free time before flights and (3) earn a bit of money.
  - I have done 2 NLP projects before, one about text classification in financial domain (which turns out to require a more similar skillset as this project), and one in learning *embeddings* in source code.
- Problem: 
  - Given two tables recording (intendedly) all medicines in Vietnam's pharmaceutical market.
    - The first table comes from a government official source, written mostly in Vietnamese, with ~45K rows and ~20 columns.
    - The second table comes from a market research agency who also manually captured the market. It has ~90K rows and ~25 (slighyly different) columns, and was written in (very concise and "notational") English.
    - They overlap and complement each other quite a bit.
    - (More description below)
  - It is of business interest to "match" items from these two tables together.
    - Doing this would create a larger (more rows) and richer (more columns) dataset about the market, which would eventually be use for (1) market trend analysis and (2) adhoc lookup of some specific medicine.
  - Research question: How to do that?! How to *effectively group* identical items from both tables together? A matching group has at least one item from each table, which both refer to the same real-life medicine.
    - Optimization metrics include precision, recall, development time, and system reusability.
  - This problem is a bit analogous to [Coreference Resolution](/_posts/2023-08-02-coreference-resolution.md) because the goal is also to determine groups of things that refer to the same real-world entity. Therefore, we cast it to a classification problem -- determining whether two items, each of which from a table, are refencing two the same actual medicine.
- The data is quite messy.
  - Out of 20 and 25 columns from each table, six of them are explicitly shared, including:
    - product name (e.g., "GILOBA PHYTOSOME" or "Giloba")
    - manufacturer name (e.g., "MEGA LIFESCIENCES" or "Mega Lifesciences Public Company Limited")
    - molecule (e.g., "GINKGO BILOBA" or "Cao ginkgo billoba (dưới dạng ginkgo biloba phytosome) 40mg")
    - pack strength (e.g., "40MG" or "40mg")
    - pack form (e.g., "SOFTCAP" or "Viên nang mềm")
    - unit pack (e.g., "30" or "Hộp 3 vỉ x 10 viên")
  - The shared columns are usually written in very different ways, and the syntaxes varied a lot. 

*To be continued...*

<!-- ## Methods

Show the pipeline (draw and write about)
- from data input
- to matching output


pipeline is data centric, not operation centric (like algo)?

## Results
- Performance: 0.5s per MR item, in a 7-core parallelization setting.
- Precision: 90%?
- Recall: probably 70%, which is 21K over 30K items.

## Discussion
- New things learned
  - For ML projects (which often works with real data), the ML engineers/scientists must do some labelling, or at least debugging with wrong predictions (i.e., post-mortem analysis) to really know the characteristics of the data.
  - In real projects, labelled data is usually unavailable, which renders supervised learning approaches costly.
- Remaining questions
  - Labelled data is so important in doing Machine Learning. However, labelling data is costly (and sometimes boring).
  - How to approach the clustering aspect
  - How to improve the aggregation of subscores? -->