---
title: "HTB: OpenAdmin"
author: ["Trae Horton" | "https://sorsnce.com"]
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

```
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

```
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

```
root@kali:~/HTB/red-team/HTB/Beta# msfconsole
[-] ***rtinG the Metasploit Framework console...\
[-] * WARNING: No database support: No database YAML file
[-] ***

Call trans opt: received. 2-19-98 13:24:18 REC:Loc

     Trace program: running

           wake up, Neo...
        the matrix has you
      follow the white rabbit.

          knock, knock, Neo.

                        (`.         ,-,
                        ` `.    ,;' /
                         `.  ,'/ .'
                          `. X /.'
                .-;--''--.._` ` (
              .'            /   `
             ,           ` '   Q '
             ,         ,   `._    \
          ,.|         '     `-.;_'
          :  . `  ;    `  ` --,.._;
           ' `    ,   )   .'
              `._ ,  '   /_
                 ; ,''-,;' ``-
                  ``-..__``--`

                             https://metasploit.com


       =[ metasploit v5.0.62-dev                          ]
+ -- --=[ 1950 exploits - 1090 auxiliary - 334 post       ]
+ -- --=[ 558 payloads - 45 encoders - 10 nops            ]
+ -- --=[ 7 evasion                                       ]

msf5 > search OpenNetAdmin
[-] No results from search
msf5 >
```

It appears at the time of writing this report, this exploit is not in Metasploit's database by default. We can try updating the database but more than likely it will not pull the latest copy of this exploit. Let's manually add this exploit to our Metasploit instance by using the following code:

```
root@kali:~# wget https://www.exploit-db.com/raw/47772
--2020-01-21 15:11:24--  https://www.exploit-db.com/raw/47772
Resolving www.exploit-db.com (www.exploit-db.com)... 192.124.249.8
Connecting to www.exploit-db.com (www.exploit-db.com)|192.124.249.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3017 (2.9K) [text/plain]
Saving to: ‘47772’  
47772                         100%[=================================================>]   2.95K  --.-KB/s    in 0s
2020-01-21 15:11:24 (20.4 MB/s) - ‘47772’ saved [3017/3017]
root@kali:~# mkdir -p ~/.msf4/modules/exploits/custom
root@kali:~# mv 47772 ~/.msf4/modules/exploits/custom/ona.rb
```

# Exploiting

I utilized a widely adopted approach to performing penetration testing that is effective in testing how well the Offensive Security Exam environments is secured.
Below is a breakout of how I was able to identify and exploit the variety of systems and includes all individual vulnerabilities found.

## Place-Holder

The information gathering portion of a penetration test focuses on identifying the scope of the penetration test.
During this penetration test, I was tasked with exploiting the exam network.
The specific IP addresses were:

**Exam Network**

- 192.168.
- 192.168.
- 192.168.
- 192.168.
- 192.168.

# Privilege Escalation

*Additional Priv Esc info*

**Vulnerability Exploited:**

**Vulnerability Explanation:**

**Vulnerability Fix:**

**Severity:**

**Exploit Code:**

**Proof Screenshot Here:**

**Proof.txt Contents:**

### System IP: 192.168.x.x

#### Service Enumeration

Server IP Address | Ports Open
------------------|----------------------------------------
192.168.x.x       | **TCP**: 1433,3389\
**UDP**: 1434,161

**Nmap Scan Results:**

*Initial Shell Vulnerability Exploited*

*Additional info about where the initial shell was acquired from*

**Vulnerability Explanation:**

**Vulnerability Fix:**

**Severity:**

**Proof of Concept Code Here:**

**Local.txt Proof Screenshot**

**Local.txt Contents**



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
