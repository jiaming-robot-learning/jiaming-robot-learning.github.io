---
title: Set up remote server for VScode
date: 2023-01-10 14:30:00 +0800
categories: [Ubuntu]
tags: [ubuntu]     # TAG names should always be lowercase
---

## Setup key pair on remote server
Generate rsa key pair on local PC:
```
ssh-keygen
ssh-copy-id username@remoteserver # copy pub key to remote server
```

## Setup remote 
- Install 'remote-ssh' extension in vscode
- Click the icon on the left corner and connect to the remote server

Voilà!
