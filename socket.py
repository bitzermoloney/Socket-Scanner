import socket # the socket module can be used to attempt TCP connection to IP address ports
import ipaddress # the ipaddress module can be used to generate all the active IP addresses in a subnet

network = ipaddress.ip_network("192.168.1.0/29") # We use the .ip_network() function to find the active addresses in a subnet

for host in network.hosts():
    for port in [22,80,443]: # For each host, for each of the commonly opened ports:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5) # Attempting TCP connection

        if sock.connect_ex((host, port)) == 0: # Calculating results
            print(f"Port {port} is open") # Presenting results

        sock.close()

# end