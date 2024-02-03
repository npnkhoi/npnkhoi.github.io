---
layout: post
title: Amazing Algorithms class
tags: cs
---

I just felt like I hitting the jackpot as I stumbled upon [Dr. Sergey Bereg](https://personal.utdallas.edu/~sxb027100/)'s class on *Design and Analysis of Computer Algorithms* ([class notes](https://personal.utdallas.edu/~sxb027100/cs6363/notes.htm)). Although the course title sounds easy and algorithms are something I have learned from highschool, the content of this course is a whole new level of technical challenges! 

In his [first lecture](https://personal.utdallas.edu/~sxb027100/cs6363/intro.pdf) about asymptotic analysis of running time, he spent a great deal of time to rigorously prove the complexity membership of functions. He wrote on the board so many maths, and also speak aloud a lot more maths. Key takeaways include: 
- Big-Oh and big-Omega are about *bounds*, while small-oh and small-omega formalize the saying "*this function grows faster than that*". Therefore, small notations are stronger than big notations.
- Small-oh and small-omega are actually defined via $$c$$. The limit-based definitions are theorems.
- Tricks to quickly find a loose bound for big-Oh and big-Theta proofs.
- $$\lg(n!) = \Theta(n\lg n)$$.
    - Proof 1: Apply Stirling approximation
    - Proof 2: Via big-Oh and big-Omega. Big-Omega is a bit tricky.

And this is our [first homework](/assets/h1.pdf) -- particularly like the last two problems. 

P/S: I "impressed" Dr. Bereg by catching trivial typos on slide 13 of the lecture and let him know after class.