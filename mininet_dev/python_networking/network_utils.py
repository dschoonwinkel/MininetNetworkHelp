import subprocess

def get_first_IPAddr():
	result = subprocess.check_output(["ifconfig"])
	# print 'output = %s' % result

	if result:
		addr_index = result.find("inet addr:")
		ip_addr = result[addr_index + len("inet addr:"):]
		ip_addr = ip_addr[:ip_addr.find(" ")]
		
		return ip_addr

def get_first_HWAddr():
	result = subprocess.check_output(["ifconfig"])
	# print 'output = %s' % result

	if result.find("HWaddr") == -1:
		print("HW Addr not found, using default")
		return "00:00:00:00:00:00"

	elif result:
		addr_index = result.find("HWaddr ")
		hw_addr = result[addr_index + len("HWaddr "):]
		hw_addr = hw_addr[:hw_addr.find(" ")]
		
		return hw_addr

def get_HWAddr(ifacename):
	result = subprocess.check_output(["ifconfig", ifacename])
	# print 'output = %s' % result

	if result.find("HWaddr") == -1:
		print "HW Addr not found, using default"
		return "00:00:00:00:00:00"

	elif result:
		addr_index = result.find("HWaddr ")
		hw_addr = result[addr_index + len("HWaddr "):]
		hw_addr = hw_addr[:hw_addr.find(" ")]
		
		return hw_addr


if __name__ == '__main__':
	ip_addr = get_first_IPAddr()
	hw_addr = get_first_HWAddr()
	hw_addr2 = get_HWAddr("eth0")
	print "Ip addr:", ip_addr
	print "HW addr:", hw_addr
	print "Eth0 HW addr:", hw_addr2