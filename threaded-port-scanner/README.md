# Threaded TCP Port Scanner

A fast multi-threaded TCP port scanner written in Python.

## Features

* Multi-threaded scanning
* Custom port ranges
* IP validation
* TCP connect scan

## Usage

python main.py <target_ip> -p <port_range> -t <threads>

Example:

python main.py 192.168.1.1 -p 1-1000 -t 100
