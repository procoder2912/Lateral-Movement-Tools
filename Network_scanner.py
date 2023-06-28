import scapy.all as scapy
import optparse as op

def scan(ip):
        request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        broadcast_arp = broadcast/request
       
        answered = scapy.srp(broadcast_arp,timeout=1,verbose=False)[0]
        
        macip_list = []

        for elements in answered:
                        macip = {}
                        #print(elements[1].psrc+"\t\t"+elements[1].hwsrc)
                        macip = {"ip":elements[1].psrc,"mac":elements[1].hwsrc}
                        macip_list.append(macip)

        return macip_list
def printresult(macip_list):
                print("IP\t\t\tMAC address")
                print("-------------------------------------------------")
                for macip in macip_list:
                                print(macip["ip"]+"\t\t"+macip["mac"])
                                print("-------------------------------------------------")

def getInput():
        parser = op.OptionParser()
        parser.add_option("-t","--target",dest="IP",help="Destination IP address")
        (options,arguments) = parser.parse_args()
        if not options.IP:
                print("[-] please specify the ip address, use --help for more information")
        return options



options = getInput()
if(options.IP==" "):
        print("IP address was not provided")
        exit()
list_of_mac_ip = scan(options.IP)
printresult(list_of_mac_ip)
