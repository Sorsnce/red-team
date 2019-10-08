# Certified Ethical Hacker v10

# recon-ng
Available default commands that recon-ng will use.
```
[recon-ng][default] > help

Commands (type [help|?] <topic>):
---------------------------------
back            Exits the current context
dashboard       Displays a summary of activity
db              Interfaces with the workspace's database
exit            Exits the framework
help            Displays this menu
index           Creates a module index (dev only)
keys            Manages third party resource credentials
marketplace     Interfaces with the module marketplace
modules         Interfaces with installed modules
options         Manages the current context options
pdb             Starts a Python Debugger session (dev only)
script          Records and executes command scripts
shell           Executes shell commands
show            Shows various framework items
snapshots       Manages workspace snapshots
spool           Spools output to a file
workspaces      Manages workspaces

[recon-ng][default] > 
```
Using workspaces to perform recon-ng
```
[recon-ng][default] > workspaces create calvary
[recon-ng][calvary] > workspaces list

  +------------+
  | Workspaces |
  +------------+
  | default    |
  | calvary    |
  | pfj        |
  +------------+

[recon-ng][calvary] > 
[recon-ng][calvary] > marketplace refresh
[*] Marketplace index refreshed.
[recon-ng][calvary] > marketplace install recon/domains-hosts/hackertarget
[*] Module installed: recon/domains-hosts/hackertarget
[*] Reloading modules...
[recon-ng][calvary] > modules load recon/domains-hosts/hackertarget
[recon-ng][calvary][hackertarget] > info

      Name: HackerTarget Lookup
    Author: Michael Henriksen (@michenriksen)
   Version: 1.0

Description:
  Uses the HackerTarget.com API to find host names. Updates the 'hosts' table with the results.

Options:
  Name    Current Value  Required  Description
  ------  -------------  --------  -----------
  SOURCE  default        yes       source of input (see 'show info' for details)

Source Options:
  default        SELECT DISTINCT domain FROM domains WHERE domain IS NOT NULL
  <string>       string representing a single input
  <path>         path to a file containing a list of inputs
  query <sql>    database query returning one column of inputs

[recon-ng][calvary][hackertarget] > options set SOURCE www.calvary.com
SOURCE => www.calvary.com
[recon-ng][calvary][hackertarget] > run

-------------------------------
WWW.CALVARY.COM
-------------------------------
[*] [host] www.calvary.com (66.77.51.230)

-------
SUMMARY
-------
[*] 1 total (1 new) hosts found.
[recon-ng][calvary][hackertarget] > 

```

Using modules within recon-ng
```
[recon-ng][calvary] > modules search

  Recon
  -----
    recon/domains-contacts/whois_pocs
    recon/domains-hosts/hackertarget

[recon-ng][calvary] > 
```
# maltego

# nmap
Make sure you remember and understand the following nmap flags for the CEH:
```
-sS = TCP SYN/Connect Scan
-sn = Ping Scan
```
```
$ nmap -sS 192.168.1.0/24
```
# netdiscover
```
$ sudo netdiscover

Currently scanning: 172.16.34.0/16   |   Screen View: Unique Hosts                                                                         
19 Captured ARP Req/Rep packets, from 3 hosts.   Total size: 1140                                                                          
_____________________________________________________________________________
  IP            At MAC Address     Count     Len  MAC Vendor / Hostname      
-----------------------------------------------------------------------------
192.168.8.1     00:50:56:c0:00:08     17    1020  VMware, Inc.                                                                             
192.168.8.2     00:50:56:fa:26:a6      1      60  VMware, Inc.                                                                             
192.168.8.254   00:50:56:f5:a3:c3      1      60  VMware, Inc.                                                                           

```

# hping

# hydro

# cherrytree

# foca

# metasploit
```
$ sudo service postgresql status
$ sudo msfdb status
$ sudo msfconsole
```
