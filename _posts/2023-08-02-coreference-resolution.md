---
title: Coreference Resolution
layout: post
---

So I am reading about *coreference resolution* (CR), a topic that my potential PhD advisor has many contributions in. CR is the task of determine the nounphrases in a text that points to the same real-world entity and phenomenon. You may understand this definition but have difficulties to appreciate its importance. I was at the same situation. It turns out, arguably the most notable application of CR is in information retrieve and question answering. Consider the following paragraph:

*"This is Khoi. He is handsome."*

Imagine a robot reads this text and is asked "Who is handsome". While finding the answer in the text, the robot found the second sentence with the word "handsome". But who is handsome? "He"! Well, that's not a good answer. A better answer is "Khoi", found by associating "he" with "Khoi" as they *coreference* to the same physical entity.

On this definition, I am recognizing this is a [Saussurian](https://en.wikipedia.org/wiki/Ferdinand_de_Saussure) way of defining languages via the *signifier* and the *signified*. However, I think that framework can not be applied into abstract "objects" like patriotism. Is the word "patriotism" signifying anything real entity? No, it is concerned about an abstract concept that may further points at other entities.

**Background.** There is a prerequisit topic to know before CR, which is *named entity recognition* (NER). It is simply because CR assumes we already know at least what are the nounphrases. NER is the task of tagging each word in a text with its "high-level description". For example, "Khoi" is a name of a person, "handsome" is an adjective. That is NER. There are two major techniques for NER, which is Hidden Markdov Model (which I know and can implement!) and Conditional Random Field (which I was trying to understand during an internship last summer but have not been able to).

**Methods.** Let's be reminded that the end goal of CR is to *clutster* the nounphrases based on the real entities they are referring to. So what would be an approach for this CR task? There are basically 3 approaches. The simplest one, called *mention-pair*, is to consider all the pairs of nounphrases and check if they are coferencing. This is a classification task, and was historically done by manual feature engineering [1]. There are of course recent breakthroughs, probably with self-supervised learning () and pretrained Transformers (I guess). The other two approaches are *mention-ranking*, which is to rank the preceding nounphrases (mentions) by its likelihood to be the true antecedant (the preceiding coreferrring nounphrase), and *entity-mention*, which I did not have a chance to comprehend.

**References.**

[1] V. Ng and C. Cardie, “Improving Machine Learning Approaches to Coreference Resolution,” in Proceedings of the 40th Annual Meeting of the Association for Computational Linguistics, Philadelphia, Pennsylvania, USA: Association for Computational Linguistics, Jul. 2002, pp. 104–111. doi: 10.3115/1073083.1073102.

[2] https://www.youtube.com/watch?v=rpwEWLaueRk -- a video lecture of prof. Manning, where I learned most about CR