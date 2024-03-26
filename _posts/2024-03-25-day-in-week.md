---
layout: post
title: What date is today?
tags: math
---

"What date is today? 21 or 22" is a common type of questions to ask in daily lives. Usually, one may just look at the calendar, their computer, their watch, or their smartphone to know the answer. What if you don't want to look at digital things at the moment? What if you are in a situation where those devices are not accessible? What if you don't remember the date of any recent days at all? What if you do remember the date of Monday last week, but you don't want to use your fingers to count? You only need to remember _one_ magic number.

## The magic number to know what date today is

Every month, there is a magic constant, which is an integer from 0 to 6. That constant is the remainder of $$1 - d_1$$ divided by 7, where $$d_1$$ is the numerical value of the _day in week_ of the first day of the month. Note that "the remainder of X divided by 7" is also called "X mod 7".

$$ \text{magic number } (M) = (1-d_1) \mod 7 $$

For example, the first day of March 2024 is a Friday, and Friday is 6.[^1] Therefore, the magic constant of March 2024 is 1-6 mod 7, which is -5 mod 7, which is 2[^2]. 

Now, to know the date, given the day in week, **just add the day in week with the magic constant, then mod 7**. The date (in month) of that day must have the same mod 7.

For example, what date is this Friday? As a conscious being, I should know that it was the 20th recently, but I am not entirely sure if today is 23, 24 or 25. So, I will take Friday + Magic Constant (of this March), which is 6 + 2 = 8 = 1 (mod 7). So that day must gives 1 when mod 7. Between 20 and 31, there is only two numbers for that: 22 and 29. 22 is too close to today (Monday), so it must be 29.

$$\textrm{the date of today} \equiv \text{day in week of today} + M \mod 7$$

Is it right?

![](/assets/calendar.png)

_Yes, it is right :)_

## Magic number of next month?

When a new month comes, we need to update our magic number.

Let the old magic number be $$M$$, and the number of days of the current month be $$D$$. Then the magic number of next month is:

$$(M-D) \mod 7$$

For example, the magic number of April is $$2-31 \equiv -29 \equiv -1 \equiv 6 \mod 7$$. So April 1 will be (wait for it) $$1-6 \equiv -5 \equiv 2$$, which is a Monday!

## Summary

It looks complicated, but it is actually fast to do in your head[^3]:

- For every month, get the magic number $$M$$ (we have two ways!).
- The date of today $$\equiv \text{day in week of today} + M \mod 7$$

What is better than obtaining universal knowledge by yourself, instead of being dependent on some external source all the time?

**Footnotes:**

[^1]: Sunday is 1, Monday is 2, ..., Saturday is 7 (or 0).
[^2]: Obtained by adding 7 to -5.
[^3]: Ok, I admit it is convoluted. But it requires minimal memorization, no? And it is cool because you can do it all in your head! And having a magic number that has a real use is also cool :)