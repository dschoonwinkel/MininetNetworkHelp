#! /usr/bin/python

from scapy.all import *
import sys
import time

interface = "h1-eth0"
dest_ip = "10.0.0.2"
ip_seq_nr  = 1

def build_packet(encoded_packet_details, packet_payloads, reports, acks, payload):
	out_str = str()
	#Set the ENCODED_NUM
	out_str += str(len(encoded_packet_details)) + "\n"

	#Set the PKT_ID and NEXTHOP for each packet
	for i in range(len(encoded_packet_details)):
		out_str += hash(str(encoded_packet_details[i][0]) + str(ip_seq_nrs[i][1])) + "\n"
		out_str += dst_ips[i] + "\n"

	#Set the REPORT_NUM
	out_str += str(len(reports))

	for j in range(len(reports)):



sendp(Ether(dst="ff:ff:ff:ff:ff:ff")/IP(dst=dest_ip)/UDP(sport=9000, dport=9000)/(p1), iface=interface)
