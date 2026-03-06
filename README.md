# Offensive Security Toolkit

A collection of Python tools built while learning cybersecurity and penetration testing.

## Tools

### Threaded Port Scanner

A multi-threaded TCP port scanner capable of scanning custom port ranges.

Features:

* Multi-threaded scanning
* Custom port ranges
* IP validation

Example:

python main.py 192.168.0.1 -p 1-1000 -t 100

---

### Banner Grabber

A tool that connects to open ports and retrieves service banners.

Example output:

[+] Port 22 OPEN
Banner: SSH-2.0-OpenSSH_6.6.1

[+] Port 80 OPEN
Banner: Apache/2.4.7

---

More tools will be added as the toolkit grows.
