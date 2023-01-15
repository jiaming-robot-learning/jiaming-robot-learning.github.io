---
title: Use multiple github account
date: 2023-01-15 16:32:35 +0800
categories: [Productivity]
tags: [git, ssh]
---

### Setup key on github (optional)
Generate key pairs on local machine and copy public key to github
```
ssh-keygen
```

### Edit ssh config
```
# on local machine
vim ~/.ssh/config
# add following lines to the file and save
Host <git-name> 
     HostName github.com
     User <github account name/email>
     IdentityFile <private key generated>
```

### Clone repository
Use the following command to clone git repositories
```
git clone git@\<git-name\>:\<org-name\>/\<repo-name\>
```

### Troubleshooting
May use the following command to change github account:

```
git config --credential.username '<github-username>'
```