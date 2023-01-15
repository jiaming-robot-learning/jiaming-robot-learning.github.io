---
title: Set up remote server for VScode
date: 2023-01-10 14:30:00 +0800
categories: [Productivity]
tags: [vscode,ssh]     # TAG names should always be lowercase
---

## Setup key pair on remote server
Generate rsa key pair on local PC:
```
ssh-keygen
ssh-copy-id username@remoteserver # copy pub key to remote server
```

## Add ssh config
```
# on local machine
vim ~/.ssh/config
# add following lines to the file and save
Host <Name> 
     HostName <HostName>
     User <UserName>
     IdentityFile <PrivateKey>

# to connect to the sever <Name>, simply
ssh <Name>
```
## Setup remote ssh
- Install 'remote-ssh' extension in vscode
- Click the icon on the left corner and connect to the remote server

Voilà!
