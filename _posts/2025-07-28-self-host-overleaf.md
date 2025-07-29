---
title: "Free and unlimited scientific writing: self-hosting Overleaf"
layout: post
tags: cs academia
---

Overleaf is the de-facto standard platform for scientific writing due to its supreme support for collaborative editing in LaTeX projects. The app has been having two subscription plans: free vs paid. The Free plan has been pretty good, until when Overleaf imposes a compile time limit on projects under a Free plan. As of now, the limit is 10s, which means any compile that exceeds the limit will automatically be returned with a timeout error. Such a limit causes timeouts to happen a lot more often. Fortunately, Overleaf is not a proprietary software. That means one can hosts Overleaf in their machines for free and enjoy an Overleaf without any time limit.

This tutorial will show you how to self-host an overleaf instance.

## Ingredients

- A remote server with `docker` installed

## Steps

Server setup:

- Log into the server
- Follow the official instructions at https://github.com/overleaf/toolkit/blob/master/doc/quick-start-guide.md until “Create your first project”
- For now, the server does not have enough latex packages for normal uses. Therefore, install packages by doing the following:
    
    ```python
    # outside the container (inside SSH server)
    docker exec -it sharelatex bash
    # inside the container
    tlmgr install scheme-medium # a bundle of many packages
    tlmgr install threeparttable
    tlmgr install endnotes
    tlmgr install changepage
    tlmgr install stringstrings
    tlmgr install textpos
    tlmgr install floatrow
    tlmgr install mdframed
    tlmgr install zref
    tlmgr install needspace
    tlmgr install mfirstuc
    tlmgr install alphalph
    tlmgr install fbb
    tlmgr install sourcesanspro
    tlmgr install mathastext
    tlmgr install biblatex-chicago
    tlmgr install biblatex
    ```
    

Now Overleaf should be running! To access it, do the following in the client:

- In the terminal, run `ssh -L 8080:127.0.0.1:80 your-username@your-host-domain.com` . Replace the placeholders appropriately.
- Go to [http://localhost:8080/project](http://localhost:8080/project). You should see an Overleaf website running out of your server.

Good luck and enjoy your free unlimited Overleaf!

## Further

Useful tutorials:

- [User management](https://github.com/overleaf/overleaf/wiki/Creating-and-managing-users): How to create accounts for your collaborators to join
- [Backup](https://github.com/overleaf/overleaf/wiki/Data-and-Backups): Self-hosting Overleaf also means that you are responsible for storing the writing done by your research team. While the server’s data is persistent on the disk by default, careless server management could easily lead to data loss. As a best practice, back up the server’s data regularly.

References:

- https://github.com/overleaf/toolkit
- [https://shihabkhan1.github.io/overleaf/stepbystep.html](https://shihabkhan1.github.io/overleaf/stepbystep.html)
