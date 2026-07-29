import ipaddress # The ipaddress module can be used to find all the active addresses on a subnet

network = ipaddress.ip_network("192.168.1.0/29") # Uses the ip_network function to get the active addreses on a subnet

for host in network.hosts():
    print(host) # Outputting results 