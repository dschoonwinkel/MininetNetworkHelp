# Get info about the machine running this code
iface_name = net_utils.get_default_interface()
local_ip = net_utils.get_ip_address(iface_name)
local_mac = net_utils.get_mac_address(iface_name)
local_bcast = net_utils.get_broadcast_address(iface_name)

# Construct the ARP broadcast packet
arp = dpkt.arp.ARP()
arp.sha = net_utils.str_to_mac(local_mac)
arp.spa = net_utils.str_to_inet(local_ip)
arp.tha = net_utils.str_to_mac('00:00:00:00:00:00') # Target MAC (broadcast)
arp.tpa = net_utils.str_to_inet('192.168.1.8') # Target IP (broadcast)
arp.op = dpkt.arp.ARP_OP_REQUEST

eth = dpkt.ethernet.Ethernet()
eth.src = arp.sha
eth.dst = net_utils.str_to_mac('ff:ff:ff:ff:ff:ff')
eth.type = dpkt.ethernet.ETH_TYPE_ARP
eth.data = arp

# Create a raw socket
print 'ARP Broadcast Packet:'
print '\t- %s' % local_bcast
print '\t- %s' % iface_name
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)     

# also tried these for last arg to socket: socket.IPPROTO_RAW, socket.SOCK_RAW, dpkt.ethernet.ETH_TYPE_ARP)

# Tried lots of different combinations here (yes bind makes no sense but lots of examples had bind)
s.bind(('', 0))
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 0) #no headers
#s.bind((iface_name, socket.SOCK_RAW))
#s.connect((local_bcast, 1))
sent = s.sendto(str(eth), (local_bcast,0))
#sent = s.send(str(eth))
print sent
print repr(eth)