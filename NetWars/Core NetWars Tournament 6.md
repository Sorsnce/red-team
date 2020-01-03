# Core NetWars Tournament 6

### GOLDEN TICKET

#### Greetings to you , the lucky finder of this golden ticket, from Mr. Willy Wonka!
I shake you warmly by the hand! Tremendous things are in store for you! Many wonderful surprises await you! For now, I do invite you to come to my factory and be my guest for two evenings - you and all others who are lucky enough to nd my Golden Tickets. I, Willy Wonka, will conduct you around the factory myself, showing you everything that there is to see.

I am preparing other surprises that are even more marvelous and more fantastic for you and for all my beloved Golden Ticket holders - mystic and marvelous surprises that will entrance, delight, intrigue, astonish, and perplex you beyond measure!

Present this ticket at the factory gates at six thirty in the evening of the rst day of NetWars. Don't be late! And you are allowed to bring with you members of your team to look after each other and to ensure that you don't get into mischief. One more thing - be certain to have your conference badge with you, otherwise you will not be admitted.

(Signed) Willy Wonka


## Objective: WW - A Golden Ticket 

**Q1 - I GOT A GOLDEN TICKET**

What user account are you automatically logged into in the provided virtual machine?


**A1 - 'contestwinner'**
```
contestwinner@oompa-loompa:~$  whoami
contestwinner
```
________________________________________________________________________________________________________________________________________

**Q2 - DOOMPADEE DOO**

What's the host name of your workstation?


**A2 - 'oompa-loompa'**
```
contestwinner@oompa-loompa:~$ hostname
oompa-loompa
```
________________________________________________________________________________________________________________________________________

**Q3 - AN ODD PATH**

When a user enters a command into a Windows command prompt or a Linux terminal, the operating system checks for commands and programs of that name in the environment “path” . The $PATH / %PATH% variable tells the OS where to look for the command entered.
Your system has something odd in its path. What is it?


**A3 - '/usr/bin/wonkafactory'**
```
contestwinner@oompa-loompa:~$ echo $PATH
/home/contestwinner/.rvm/gems/ruby-2.4.6/bin:/home/contestwinner/.rvm/gems/ruby-2.4.6@global/bin:
/usr/share/rvm/rubies/ruby2.4.6/bin:/home/contestwinner/bin:/home/contestwinner/.local/bin:
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:
/snap/bin:/pentest/exploitation/burp/:/usr/bin/wonkafactory/:/usr/share/rvm/bin
```
________________________________________________________________________________________________________________________________________
**Q4 - IMPROVED!**

What version of VI IMproved is available on your workstation? 

Please answer in the form **\<major version>.\<minor version>**, eg **1.2**


**A4 - '7.4'**
```
contestwinner@oompa-loompa:~$ vim --version
VIM - Vi IMproved 7.4 (2013 Aug 10, compiled Jun 07 2019 15:35:43)
```
________________________________________________________________________________________________________________________________________
**Q5 - EDIBLE SIT-ABLES**

Whose toadstool is that? in your user's home directory (/home/contestwinner/), 
there is a text file called toadstool.txt. Which user is able to write to this file?


**A5 - 'mike'**
```
contestwinner@oompa-loompa:~$ ls -l
-r--rw----  1 contestwinner teavee               62 Nov  6 16:37 toadstool.txt
contestwinner@oompa-loompa:~$ cat /etc/group | grep teavee
teavee:x:1006:mike
```
________________________________________________________________________________________________________________________________________
**Q6 - LOOMPA DAY**

When was your Oompa Loompa born? That is, on what date was your default shell/command line/terminal last modified?
Answer with a date in the format YYYYMMDD

**A6 - '20190314'**
```
contestwinner@oompa-loompa:~$ ls -l /bin/bash
-rwxr-xr-x 1 root root 1037528 Mar 14  2019 /bin/bash
```
________________________________________________________________________________________________________________________________________
**Q7 - CLASSY CHOCOLATE**

Someone is trying to sull the name of our chocolate! Inside your Oompa Loompa workstation, an image file as part of an
installed package has been modified. What's the sha1sum of the maliciously inserted file?

**A7 - ''**
```
contestwinner@oompa-loompa:~$

```
________________________________________________________________________________________________________________________________________
**Q8 - EXPRESS YOURSELF, REGULARLY**

Regular expressions can be powerful tools in everything from sed to perl to powershell . Which of these regular expressions would match these whole strings:

* Fickelgruber is 2 smelly
* Prodnose is not number 1 in our books
* Slugworth is more lame than 87 percent of society

but not these:

* Willy knows 1000000 things
* Charlie is worth over 1000 dollars or pounds
* Tom and Jerry started in the 1940s

Choose one of the folloing:
* ``` (\d|\d\d) ```
* ``` *is.* ```
* ``` [A-Za-z\s]+\d+[a-z\s]* ```
* ``` [\D]+\d{1,2}[a-z ]+ ```

**A8 - '``` [\D]+\d{1,2}[a-z ]+ ```'**

________________________________________________________________________________________________________________________________________
**Q9 - NOT ALL THAT GLITTERS**

Five Golden Tickets were found, and they’re in the tickets subdirectory of your home folder! But wait - one of them is SLIGHTLY 
different… Which one isthe fake?

* ticket1.gif
* ticket2.gif
* ticket3.gif
* ticket4.gif
* ticket5.gif


**A9 - 'ticket5.gif'**
```
contestwinner@oompa-loompa:~/tickets$ sha256sum *
d1e4bfb0686e6b550245e9a58418ec2c4a4db1cd06f5dc86455d94f60a1b99f5  ticket1.gif
d1e4bfb0686e6b550245e9a58418ec2c4a4db1cd06f5dc86455d94f60a1b99f5  ticket2.gif
d1e4bfb0686e6b550245e9a58418ec2c4a4db1cd06f5dc86455d94f60a1b99f5  ticket3.gif
d1e4bfb0686e6b550245e9a58418ec2c4a4db1cd06f5dc86455d94f60a1b99f5  ticket4.gif
ee6f375b65ddd1c3d1076026b2995d125ae1a7d86b1a580aa8dfe7ba7bb51b35  ticket5.gif
contestwinner@oompa-loompa:~/tickets$ 

```
