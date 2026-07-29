import socket # Python's socket module allows us to attempt a TCP connection

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1) # We attempt this here

result = sock.connect_ex(("192.168.1.1", 80)) # .connect_ex() returns 0 if the port is open and anything else if not...

# This is a basic check if statement
if result == 0:
    print("Port is open")
else:
    print("Port is closed")
# ...which displays the results
sock.close()