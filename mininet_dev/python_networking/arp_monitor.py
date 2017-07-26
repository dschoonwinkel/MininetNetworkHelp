#! /usr/bin/python
from scapy.all import *
import threading
import time

run_event = threading.Event()
packets = list()

class PacketWaiter(threading.Thread):
	def __init__(self, name):
		threading.Thread.__init__(self)		
		self.name = name

	def run(self):
		global packets, run_event
		while run_event.is_set():
			# print packets, "\n"
			print len(packets), "packets in buffer"
			time.sleep(10)



def arp_monitor_callback(pkt):
    if UDP in pkt: #who-has or is-at
    	global packets
    	packets.append(pkt)
    	# print "ls(pkt)",ls(pkt)
    	# print "str(pkt)", str(pkt)
        return pkt.sprintf("%IP.src% %UDP.sport% %UDP.dport%")




def main():
	try:
		run_event.set()
		waiter = PacketWaiter("waiter thread")
		waiter.daemon = True
		waiter.start()
		sniff(prn=arp_monitor_callback, filter="udp port 9000", store=0)
	except KeyboardInterrupt:
		print "Keyboard interrupt"
		run_event.clear()
	

if __name__ == '__main__':
	main()



