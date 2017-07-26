from scapy.all import sendp,Ether, Raw

# sendp(Ether(dst="ff:ff:ff:ff:ff:ff")/IP(dst="10.1.1.4")/ICMP()/"HelloWorld")
sendp(Ether(dst="ff:ff:ff:ff:ff:ff")/Raw("HelloWorld"), iface="h1-eth0", loop=1, inter=0.2)