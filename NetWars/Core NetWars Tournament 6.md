# Core NetWars Tournament 6

### GOLDEN TICKET

#### Greetings to you , the lucky finder of this golden ticket, from Mr. Willy Wonka!
I shake you warmly by the hand! Tremendous things are in store for you! Many wonderful surprises await you! For now, I do invite you to come to my factory and be my guest for two evenings - you and all others who are lucky enough to nd my Golden Tickets. I, Willy Wonka, will conduct you around the factory myself, showing you everything that there is to see.

I am preparing other surprises that are even more marvelous and more fantastic for you and for all my beloved Golden Ticket holders - mystic and marvelous surprises that will entrance, delight, intrigue, astonish, and perplex you beyond measure!

Present this ticket at the factory gates at six thirty in the evening of the rst day of NetWars. Don't be late! And you are allowed to bring with you members of your team to look after each other and to ensure that you don't get into mischief. One more thing - be certain to have your conference badge with you, otherwise you will not be admitted.

(Signed) Willy Wonka


## Objective: WW - A Golden Ticket :star:

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




## Objective: WW - Chocolate Room :star:
The challenges in this room center around the
/home/contestwinner/chocolateroom/ folder.


**Q1 - PLUMBING CHECK**

Just like pipes hauling chocolate out of our river, you can redirect the standard output of a command to the standard input of another. For example, if you 
want BEAUTIFUL le listings, try ls -l | lolcat to see what happens! You can also direct output to a le by typing something like ls -l >
/tmp/listing.txt . This will write your directory listing to a le in /tmp/ instead of showing it in your terminal. How can you have both?

Specically, which command will append the output of ls -l to /tmp/listing.txt AND print it to the terminal (standard out)?

* ls -l >> tail -f /tmp/listing.txt
* ls -l >> type -w /tmp/listing.txt
* ls -l | tee -a /tmp/listing.txt
* ls -l | top /tmp/listing.txt

**A1 - 'ls -l | tee -a /tmp/listing.txt'**
```
contestwinner@oompa-loompa:~/chocolateroom$ ls -l | tee -a /tmp/listing.txt
total 5368
drwxr-xr-x  2 contestwinner contestwinner    4096 Nov  6 16:37 buttercups
-rw-r--r--  1 contestwinner contestwinner    1497 Nov  6 16:37 effluent.bak
-rw-r--r--  1 root          root             1497 Nov  6 16:37 effluent.txt
-rwxr-xr-x  1 root          root          5435088 Nov  6 16:37 filter
drwxr-xr-x 12 contestwinner contestwinner    4096 Nov  6 16:37 row90
drwxr-xr-x 12 contestwinner contestwinner    4096 Nov  6 16:37 row91
drwxr-xr-x 12 contestwinner contestwinner    4096 Nov  6 16:37 row92
drwxr-xr-x 12 contestwinner contestwinner    4096 Nov  6 16:37 row93
drwxr-xr-x 12 contestwinner contestwinner    4096 Nov  6 16:37 row94
drwxr-xr-x 12 contestwinner contestwinner    4096 Nov  6 16:37 row95
drwxr-xr-x 12 contestwinner contestwinner    4096 Nov  6 16:37 row96
drwxr-xr-x 12 contestwinner contestwinner    4096 Nov  6 16:37 row97
drwxr-xr-x 12 contestwinner contestwinner    4096 Nov  6 16:37 row98
drwxr-xr-x 12 contestwinner contestwinner    4096 Nov  6 16:37 row99
-rw-r--r--  1 contestwinner contestwinner      57 Nov  6 16:37 scoring.json
-rw-rw-r--  1 contestwinner contestwinner       0 Jan  3 14:33 type
-rw-r--r--  1 contestwinner contestwinner      80 Nov  6 16:37 wonkatania.enc
contestwinner@oompa-loompa:~/chocolateroom$ 

```
________________________________________________________________________________________________________________________________________

**Q2 - MY LITTLE -BUTTERCUP**

Oh, there’s a buttercup ower that’s gone bad. Please rename the one in $HOME/chocolateroom/buttercups/ with a - in the le name to match the others. Once you're done, please run $ ./bc-sniff in that folder to get the ag we've tucked away for you!


**A2 - 'NetWars{YouCanEatAlmostEverything}'**
```
contestwinner@oompa-loompa:~/chocolateroom/buttercups$ mv ./-buttercup5.txt buttercup5.txt
contestwinner@oompa-loompa:~/chocolateroom/buttercups$ ./bc-sniff 
Yes yes - THANK you!
NetWars{YouCanEatAlmostEverything}
contestwinner@oompa-loompa:~/chocolateroom/buttercups$ 

```
________________________________________________________________________________________________________________________________________

**Q3 - ONE LIVE LOLLY**

One of these lollipops is actually a lever that turns some of the pipes on and off or whatever. Can you find which lollipop in your 
$HOME/chocolateroom/ folder tree is an executable program?


**A3 - 'lollipop99-44'**
```
contestwinner@oompa-loompa:~/chocolateroom$ find $HOME/chocolateroom/ -exec file {} \; | grep ELF
/home/contestwinner/chocolateroom/row99/column44/lollipop99-44: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/l, for GNU/Linux 2.6.32, BuildID[sha1]=d3bc3a83e6b748869189ea2b5eb6e4541cc45d99, not stripped
/home/contestwinner/chocolateroom/buttercups/bc-sniff: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/l, for GNU/Linux 2.6.32, BuildID[sha1]=28ba79c778f7402713aec6af319ee0fbaf3a8014, stripped
/home/contestwinner/chocolateroom/filter: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/l, for GNU/Linux 2.6.32, BuildID[sha1]=28ba79c778f7402713aec6af319ee0fbaf3a8014, stripped

contestwinner@oompa-loompa:~/chocolateroom/row99/column44$ ./lollipop99-44 
One hundred percent pure!
contestwinner@oompa-loompa:~/chocolateroom/row99/column44$ 
```
________________________________________________________________________________________________________________________________________

**Q4 - HHC FAN DETECTED**

It seems someone used your terminal to do a bit of Android app reversing. What’s the name of the file they examined?


**A4 - 'SantaGram_4.2.apk'**
```
contestwinner@oompa-loompa:~/chocolateroom/row99/column44$ history | grep ".apk"
   35  ncat 172.26.85.45 41370 > SantaGram_4.2.apk
   36  apktool -d SantaGram_4.2.apk
  194  grep *.apk
  196  history | grep "apk"
  769  history | grep ".apk"
contestwinner@oompa-loompa:~/chocolateroom/row99/column44$ 

```
________________________________________________________________________________________________________________________________________

**Q5 - GLOOP IN THE RIVER**

Parts of the factory can operate with command line redirectors. For example, the lter that looks for gloop-y substances in the chocolate
river can be tested at the terminal; there’s a version of it in the ~/chocolateroom/ folder. If you cat effluent.txt and redirect its 
output to ./filter , it’ll give you 100+ lines of output. Some of the lines will show as dropped by the lter. What’s wrong with those 
lines?

What type of attack do lines 10, 20, 30, etc. in effluent.txt resemble?
* DNS cache poisoning
* SQL injection
* Twitter handle injection
* command injection
* input bounds poisoning

**A5 - 'SQL injection'**
```
contestwinner@oompa-loompa:~/chocolateroom$ cat effluent.txt 
anisotropy
@tkh16
willy wonka blu-ray
wrt54g
Whangdoodles
Hornswogglers
Snozzwangers
' rotten Vermicious Knids '
banana
' UNION SELECT 1,2,user(),4,5; --
quote "I hope you enjoy it.  I think you will."
123456789
iloveyou
princess
@iagox86
rockyou
Mrs. Teavee
monkey
lynnie!
' UNION SELECT 1,2,user(),4,5; --

```
________________________________________________________________________________________________________________________________________

**Q5.1 - FILTER PRACTICE**

Here in our factory, we have a WWAF - Wonka Web Application Firewall! It works similarly to other modern WAF technologies. We use JSON 
rule sets to filter out good input with positive values from bad input using negative values. For example:
```
{
 "\\d":-50,
 "[a-z]":1
}
```
These rules would filter out lines with digits while keeping lines with lowercase alpha characters.

Let's practice by creating a JSON rule set le named my-rules.json that will allow every line through that doesn't have an @ symbol.

Then run ./filter -r my-rules.json < effluent.txt and (if correct) submit the hash provided.

Note: ./filter -h will show you lter options

**A5.1 - ''**
```
contestwinner@oompa-loompa:~/chocolateroom$ cp scoring.json my-rules.json
contestwinner@oompa-loompa:~/chocolateroom$ nano my-rules.json

{
  "'1'='1'"|"1=1":-50,
  "[a-zA-Z]":1,
  "\\w{5}":5
}

```

________________________________________________________________________________________________________________________________________

**Q5.2 - FILTER THE GLOOP**

That filter we have on the chocolate river does a great job keeping junk out and letting good stuff in - when it’s congured correctly.
For example, effluent.txt has some valid strings in it, but every 10th line needs to be ltered out. (You're kidding! What a crazy, 
pseudo-random happenstance!) Using scoring.json as an example, congure your own rule set of 10 rules or fewer to block those bad lines 
- and nothing else

Once you’ve achieved this, what’s the SHA1 hash of the filtered output? This hash will be printed to the console by filter .

Hint: You can test your regular expressions using sites such as https://regex101.com/ (https://regex101.com/).

**A5.2 - ''**
```
contestwinner@oompa-loompa:~/chocolateroom$ 

```

________________________________________________________________________________________________________________________________________

**Q6 - ON ENCRYPTION**

As you surely have gathered, secrecy is something we take quite seriously here! As such, it is important that you understand some of 
the essentials of cryptography. Let's start with some AES encryption.

Use openssl enc -aes-256-cbc to encrypt anything. Then look at the contents with xxd or hexdump -C . 
What are the first six characters in the file?

**A6 - ''**
```
contestwinner@oompa-loompa:~/chocolateroom$ 

```
________________________________________________________________________________________________________________________________________

**Q6.1 - SWEET INITIALIZATION VECTORS!**

If you add -p or -P to the prior openssl command, you'll notice certain values are output:

* **Salt**: A pseudo-random value that makes brute force decryption more difcult.
* **Key**: The secret, shared value that is used to encrypt and decrypt the message.
* **IV**: Ciphers like AES-CBC uses a rolling encryption scheme. You can think of an **initialization vector** as the starting point in that roll

``` openssl ``` creates a pseudo-random **salt** each time it's run. The **key** and **IV** are derived from the password the user supplies. 
If you run the command multiple times, the values change because of the **salt**.

If you tell openssl not to use a **salt**, what **IV** comes with the password ``` Nice children ``` ? Give your answer as a string of 32 hexadecimal characters.


**A6.1 - ''**
```
contestwinner@oompa-loompa:~/chocolateroom$ 

```
________________________________________________________________________________________________________________________________________

**Q6.2 - THE WONKATANIA**

We have a special way of summoning the Wonkatania when we want to oat down the chocolate river. The instructions are encrypted 
and sitting in the ``` chocolateroom ``` folder. We used **aes-256-cbc, didn’t use any padding or salt**, and the encryption 
passphrase is ``` Pure Imagination ```. It could be accomplished with **openssl** or any one of many scripting languages.

Decrypt this le and submit a SHA-1 sum of its contents.

**A6.2 - ''**
```
contestwinner@oompa-loompa:~/chocolateroom$ 

```
## Objective: WW - Inventing Room :star:
You have now come to the most interesting and, at the same time, the most secret room of my factory. Ladies and Gentlemen, 
The Inventing Room. Now remember, no messing about. No touching, no tasting, no telling.

You may be interested in trying our new Vegetable Gum. Oh no, it's not what you think. It tastes like ordinary chewing gum, 
but it smells like cauliower and asparagus to anybody else. This way, if you chew a piece after dinner, your parents will 
think you ate your vegetables!

The challenges in this room center around the
/home/contestwinner/inventingroom/ folder.


**Q1 - LIFTING WOOD**

It seems that a rogue system on our network was attempting to access SMB shares on the mail server. We're concerned that the activity 
may have been successful. You can use ```evtx_dump.py``` to parse the ```.evtx``` file into XML. Alternately, if you have a Windows 
host or VM, feel free to use PowerShell or Event Viewer to analyze the evidence.

First, please examine the file and let us know how many events were captured.

**A1 - '38'**
```
Copy the loginlog.evtx from the VM to your Windows Host
Open loginlog.evtx from the Windows Host
Count how many events were captured in loginlog.evtx
```
________________________________________________________________________________________________________________________________________

**Q1.1 - SPLITTING WOOD**

Please, analyze the log le and let us know which account was successfully leveraged to access the server! Time for a password reset...


**A1.1 - 'joe'**
```
Open loginlog.evtx from the Windows Host
If you have the Column "Task Category" visible we want to search for a Logoff event
The event before the only Logoff event should be an event for a Logon using "joe" with impersonation Level of "Impersonation"
```
________________________________________________________________________________________________________________________________________

**Q2 - LOST KEY**

There's an encrypted ```note.enc``` in $HOME/inventingroom , but we've lost the key. Here's what we remember:

* We used a null IV ('\x00')
* The encryption key was 32 bytes long, and the last 30 bytes of it were null ( \x00 )
* It was encrypted with aes-256-cbc, no salt, no PKCS7 padding
* The lowercase string stop was in the original message

The answer should be a string of characters, starting with a capital letter, and ending with punctuation.

What was the original message in ```note.enc``` ?

**A2 - ''**
```

```
________________________________________________________________________________________________________________________________________

**Q3 - EVERLASTING CONFIG FILE**

The prototype Everlasting Gobstopper Machine is currently turned off - and has been since that candy was moved to the general production 
line. Just to see if it works, please edit its config and try to start it up. Oh, just to warn you, it might be picky about the time 
stamp on that config file.

Adjust ```gs-config.txt``` to turn the machine on, and make sure its timestamp is before noon on 30 June, 1971.

**A3 - 'NetWars{VeryLittlePocketMoney}'**
```
contestwinner@oompa-loompa:~/inventingroom$ touch -t 7006301105 gs-config.txt
contestwinner@oompa-loompa:~/inventingroom$ ./gobstopper 
Attempting to turn machine ON
gs-config.txt modified time is 15591900.0
If you don't speak epoch, that's 1970-06-30 11:05:00
Machine on! 
NetWars{VeryLittlePocketMoney}
contestwinner@oompa-loompa:~/inventingroom$
```
________________________________________________________________________________________________________________________________________

**Q4 - BY GUM, IT'S GUM!**

I've dropped parts of a flag into the Dinner Gum machine. Can you examine bygumitsgum and find the original string?

**A4 - 'NetWars{ItHappensEveryTimeTheyAllBecomeBlueberries}'**
```
contestwinner@oompa-loompa:~/inventingroom$ base64 -d bygumitsgum > output
contestwinner@oompa-loompa:~/inventingroom$ file output
output: gzip compressed data, last modified: Wed Jan 23 14:53:19 2019, from Unix
contestwinner@oompa-loompa:~/inventingroom$ 

Now that we know "output" is a compressed file we will use 7zip to extract the data 
mulitple times until you get a file named "message.txt"

contestwinner@oompa-loompa:~/inventingroom$ cat message.txt
JTRlJTY1JTc0JTU3JTYxJTcyJTczJTdiJTQ5JTc0JTQ4JTYxJTcwJTcwJTY1JTZlJTczJTQ1JTc2JTY1JTcyJTc5JTU0JTY5JTZkJTY1JTU0JTY4JTY1JTc5JTQxJTZjJTZjJTQyJTY1JTYzJTZmJTZkJTY1JTQyJTZjJTc1JTY1JTYyJTY1JTcyJTcyJTY5JTY1JTczJTdk

Now use Burp Suite to decode in this order
Decode as Base64 > Decode as URL
NetWars{ItHappensEveryTimeTheyAllBecomeBlueberries}
```
________________________________________________________________________________________________________________________________________
**Q5 - OFF WE GO**

We've sewn a secret path to root privileges in your workstation with a SUID 0 setting on an executable.
Exploit this escalation path and cat the file located at /root/rules.txt .


**A5 - 'NetWars{NoTouchingNoMeddlingNoTasting}'**
```
contestwinner@oompa-loompa:~/inventingroom$ find / -perm -4000 2>/dev/null
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/eject/dmcrypt-get-device
/usr/lib/snapd/snap-confine
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/openssh/ssh-keysign
/usr/bin/ne

contestwinner@oompa-loompa:~/inventingroom$ ne
Press Escape > Now open a new file > Select /etc/sudoers > and add the following under root
contestwinner ALL=(ALL) NOPASSWD:ALL
Now save the /etc/sudoer file
contestwinner@oompa-loompa:~/inventingroom$ sudo /bin/bash
root@oompa-loompa:~/inventingroom# cat /root/rules.txt 
NetWars{NoTouchingNoMeddlingNoTasting}
root@oompa-loompa:~/inventingroom# 

```
________________________________________________________________________________________________________________________________________
**Q6 - FIXING A HOLE**

There's a hole in the lickable - I mean uncomplicated - rewall, and we're concerned about our snozzberries!

With UID 0 privileges (as root), please use ```ufw``` to fix the hole - delete the rule that allows TCP/50413 in. Once it's patched up, 
look in /root/ for the flag we'll drop.

**A5 - 'NetWars{ItTastesLikeSnozzberries}'**
```
root@oompa-loompa:/root# sudo ufw delete allow 50413/tcp

```
________________________________________________________________________________________________________________________________________

## Objective: WW - Fizzy Lifting Drink Room :star: :star:
Something very unusual in here. Bubbles, bubbles everywhere, but not a drop to drink. Yet.

There are our Fizzy Lifting Drinks. They fill you with gas, and the gas is so terrically lifting that it lifts you right off the 
ground like a balloon. But I daren't sell it yet. It's still too powerful.

Come along now; don't hang about. You're going to be wild about this next room.

The challenges in this room center around the
/home/contestwinner/fizzyliftingdrinkroom/ folder.

________________________________________________________________________________________________________________________________________
**Q1 - STRANGE ROOM**

For some reason, this room reminds me of the windows in my dentist's ofce. Maybe it's the smell...

As root , run **/home/contestwinner/fizzyliftingdrinkroom/enter.sh** to proceed.

What directory do you start in? Answer in the form of /folder

**A1 - '/home'**
```
root@oompa-loompa:~/inventingroom# /home/contestwinner/fizzyliftingdrinkroom/enter.sh
PowerShell 6.2.3
Copyright (c) Microsoft Corporation. All rights reserved.

https://aka.ms/pscore6-docs
Type 'help' to get help.

PS /home> pwd

Path
----
/home

PS /home> 
```