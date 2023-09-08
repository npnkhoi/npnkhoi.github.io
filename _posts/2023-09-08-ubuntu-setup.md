---
layout: post
title: My Minimal Ubuntu Setup
---

After the [catastrophic failure]({%post_url 2023-09-05-digital-world%}) of Ubuntu on my laptop, I got some help from the IT office of my unversity and realized my laptop was actually not 'bricked' yet. After some efforts to revive the OS without losing personal files, I decided to erase everything and reinstall the OS again with my USB stick because the offline files on the computer is not that important anyway. And it is now alive again! But now I faced a new problem -- setting up the computer again. I wanted to be mindful about my installations, trying not to install uncessary things, and taking notes of them. I will my installations after the last 2 days below.

## Install via Ubuntu Software
- **VSCode**: for programming (main work). Logged in, and synced it
- **Bitwarden Desktop**: to quickly fill passwords in a browser-inpendent manner, to easily access other online portals
- **Chrome**: to sync all my internet activities. Logged in to various services as I go.
- **Zotero** ([good tutorial](https://www.zotero.org/support/installation)): to sync my papers. Installed Better BibLatex manually, then export them to integrate with Obsidian.
- **Obsidian**: for note taking in cross-referencing style. It has excellent syncing power. Used the .deb file for installation, then clone my note repo from Github.

## Install via `apt`
- **`git`** (then config user.email and user.name for pushes) and [`ssh`](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) (with a passphrase!): for saving code and text files online easily
- **`pip`**, and other python packages
- **`miniconda`**

## Misc
- **`vim`**: just for my geeky writing hobby :)
- **`nvidia-utils-510`** (but still have errors): for working with nvidia graphical card locally -- not very necessary...
- **Printer driver** (just go directly to the manufacturer's website, get a tar.gz, extract, run ./install.sh): to print!
- **My class materials**, put into a folder on Desktop.

## Final Reflections

- Something is just nice to have  but that is not essential, like the feeling of owning a powerful powerful hardware and being able to see their performances (CPU, GPU, etc.). But I don't install benchmarking software now. I am tired of reinstallations, of repetitions. I have attachment issues (with technology!) now.
- I don't think I need to make my computer looks interesting also. Let's normalize a boring computer for a more interesting physical life!
- Also, careless installations of many software does slow the machine down. It is actually an art to install just enough software to make your computer convenient while not slowing it down too much.
<!-- - I decided to buy the macbook BEFORE Silver broke because I wanted more speed, higher reliability and solid physical design. -->