---
title: "Streamlit + Google Cloud is a cost-free and easy-to-deploy stack for hobbyists in 2025"
layout: post
tags: cs
---

## context

Been spending my Sundays to build an app that visualizes my expenses by reading through banking screenshots. It needs an LLM inference provider, a server, and a nice programming framework to minimize typing work. The demads for such kinds of stacks is omnipresent nowadays.

After some experimentation, I want to share my thoughts about a stack that contains Google AI, Firestore, and Streamlit. It is completely free to build things on and is pleasant to work with. 

![image.png](/assets/streamlit-arch.png)

## how this stack handles things

### fronend + backend: streamlit

- streamlit is very simple but surprisingly effective
    - it takes extremely few lines of code to create a UI component, and just a few more lines of code to get it to function
    - the design of the UI components were well thought out, so I almost never have to worry about styling while coding in this framework. For reference, when I am coding in React, I have to take care of very single pixels, and the plethora of console errors that it spits out. Streamlit has almost no weird errors, no requirements for CSS micro-management.
- it also handles both fronend and backend.
    - if you really think about it, for apps without scaling requirement (i.e., the need to server the app for many users at the same time), why should it be split into frontend and backend? This insight was inspired by [DHH](https://www.youtube.com/watch?v=vagyIcmIGOQ).
    - streamlit’s monolithic architecture frees up the hassle to manage two separate servers for a small app — it says “one app, on server”
- to deploy, just click the deploy button and choose [Community Cloud](https://streamlit.io/cloud) option to host the app for free in a `streamlit.com` subdomain. Under the hood, it links to our github account, and creates a CI/CD workflow for the repo: as soon as the code is pushed to Github, the web app is rebuilt on Streamlit’s server and rebooted for all users. (The deploy time is quite low.)
    - secrets are easy and intuitive to manage
    - debugging is also easy by either looking at the friendly server log or printing things out to the UI (which looks beautiful)
    - streamlit evens links the app with a github codespace for cloud-based web development

Considered alternatives: Dash (requires more lines of code, little deployment support), React + some backend (too much work, slow, even though powerful)

Have not considered: Gradio (now owned by huggingface, can be deployed to HF Spaces)

### memory and storage: streamlit’s session state + firestore

- A lot of things can be stored in the browser ([OneSchedule](https://npnkhoi.github.io/oneschedule/#/) doesn’t have a database and can still serve 1000 users, chatgpt does not need a database for 90% of its use cases). In those cases, `st.session_state` — which manages memory using a browser tab’s memory — is enough. Again, the API is simple.
- Google Cloud gives 1GB of [free](https://cloud.google.com/free/docs/free-cloud-features#firestore) Firestore storage for every project, without asking for a credit card. This is more than enough to store some text-based data presistently for the first thousand users.

Good alternatives: MongoDB Free tier (as simple as Firestore)

Bad alternatives: a linked Google Sheet (brittle), an self-host SQL database (complicated)

### LLM: Google AI

Someone said that in the near future, AI (cloud-based) compute will be seen as essential as water and electricity. That also means it will be negligibly cheap. Is it actually cheap at the moment? The answer is yes.

Google AI Studio currently offers most of its models [for free](https://ai.google.dev/gemini-api/docs/pricing), including [Gemini 2.5](https://arxiv.org/abs/2507.06261). The [rate limits](https://ai.google.dev/gemini-api/docs/rate-limits) are also generous. Note that, Gemini 2.5 models are very powerful (great reasoning) and versatile (works with vision, language, and audio).

Good alternatives: Lightning AI deployments ($15 free every month, good for deploying custom models), HF Inference (cheap pay-as-you-go open-source models)

Probably bad alternatives: AWS Bedrock (not free), Azure AI (not free), OpenAI (not free)

## scaling capability?

- This stack should work for multi users out of the box.
- Not sure how many users it will scale to, but that doesn’t matter much for hobbyists.

## a note on vibe coding

- I originally relied on Agent mode of VS Code and Cursor to help me build the app. The first 1 hour was nice, it builds things very fast, and I thought I would not need to go through streamlit documentation any more.
- However, beyond that 1 hour, things were terrible. I lost track of the codebase, not knowing where to debug because (1) I don’t know the framework, and (2) I do not understand the data and control flows of the code.
- My working model for vibe coding is via the Ask mode (instead of the Agent mode). I need to type things down myself in order to make informed decisions and have grounded inspirations for what to do next.
- For AI coders to be more autonomous, more needs to be done in the HCI front: How to align the machine and humans? Given the human’s ideas and problems (e.g., recorded in a Notion board), how can the machine understand their intent properly and be aware of what it doesn’t know? How can humans, without being aware of every single line of code, keep up with the code base? The objective now should be to maximize the abstraction level of the coding interface while giving humans sufficient control over the codebase (in many cases, means an understanding of 99% of what the code does).

Lastly, I will be discretely releasing the expense tracking app mentioned at the beginning in a near future. It is secure, fast, pretty, web-based, and mobile-friendly. If you are interested in trying it out, shoot me a message ;)
