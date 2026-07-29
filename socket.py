import socket # The socket module can be used to attempt a TPC connection

ip = "192.168.1.1" # The address is best saved as a var because we call it a lot

for port in [22, 80, 443]: # For each of the commonly open ports...
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5) # We are attempting a connection...

    if sock.connect_ex((ip, port)) == 0:
        print(f"Port {port} is open") # And displaying results

    sock.close()