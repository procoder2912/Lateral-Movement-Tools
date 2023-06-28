import subprocess
import optparse
import re 

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i","--interface",dest="Interface",help="Interface to change mac address")
	parser.add_option("-m","--mac",dest="new_mac",help="New mac address")
	(options,arguments) =  parser.parse_args()
	if not options.Interface:
		parser.error("[-] Please specify the interface,use --help for more info")
	elif not options.new_mac:
		parser.error("[-] Please specify the New mac address, use --help for more info")

	return options


def Change_Mac(interface,new_mac):
	print("[+] Changing th mac address for "+interface+" to "+new_mac)
	subprocess.call(["ifconfig",interface," down"])
	subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
	subprocess.call(["ifconfig",interface,"up"])

def get_current_mac(interface):
	ifconfig_result = subprocess.check_output(["ifconfig",interface])
	mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig_result))
	if mac_result:
        	return mac_result.group(0)	
    else: 
       print("[-] Could not read the mac address")



options = get_arguments()

curr_mac = get_current_mac(options.Interface)
print("Current MAC address "+ str(curr_mac))
Change_Mac(options.Interface,options.new_mac)

curr_mac = get_current_mac(options.Interface)
if curr_mac == options.new_mac:
	print("[+] Mac address changed to "+curr_mac)
else:
	print("Mac address did not get changed")


