---
title: "HTB: OpenAdmin"
author: ["Trae Horton", "sorsnce.com"]
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
<p align="center">
  <img src="https://github.com/Sorsnce/red-team/blob/master/HTB/Beta/OpenAdmin.png?raw=true" alt="Sublime's custom image"/>
</p>

# Hack the Box: OpenAdmin

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
- find


# Scanning/Enumeration

Target: `10.10.10.171`

```
traeh@kali:~$ sudo nmap -sS 10.10.10.171
Starting Nmap 7.80 ( https://nmap.org ) at 2020-01-19 20:09 EST
Nmap scan report for 10.10.10.171
Host is up (0.067s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 1.22 seconds
traeh@kali:~$ 
```

Lets view what we can see on TCP Port 80:
<p align="center">
  <img src="https://github.com/Sorsnce/red-team/blob/master/HTB/Beta/apache.png?raw=true" alt="Sublime's custom image"/>
</p>

Now that we know there is a web server running on TCP port 80 lets perform a DirBuster:

```

```

## Place-Holder

I recommend patching the vulnerabilities identified during the testing to ensure that an attacker cannot exploit these systems in the future.
One thing to remember is that these systems require frequent patching and once patched, should remain on a regular patch program to protect additional vulnerabilities that are discovered at a later date.



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
