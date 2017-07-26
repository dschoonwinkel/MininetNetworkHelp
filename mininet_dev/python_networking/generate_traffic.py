#! /usr/bin/python

from scapy.all import *
import sys
import time

interface = "eth0"
dest_ip = "10.0.0.1"
if len(sys.argv) >= 2:
	interface = sys.argv[1]

if len(sys.argv) >= 3:
	dest_ip = sys.argv[2]

for i in range(5):
	sendp(Ether(dst="ff:ff:ff:ff:ff:ff")/IP(dst=dest_ip)/UDP(sport=9000, dport=9000)/(str(90) + "HelloWorld"), iface=interface)
	time.sleep(0.5)
