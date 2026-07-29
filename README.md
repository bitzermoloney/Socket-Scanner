# Socket-Scanner
This program takes an IP address of a subnet, tries to determine which hosts are online, checks whether common TCP ports are open and displays the results.

# Information
As an undergraduate in CS with Cyber Security (CSCS), I decided my next project should be surrounding networks and network security. This project aims to expand my skills in python networking.

# Planning
This project will need to:
1. Take an IP address or subnet.
2. Determine (or try to determine) which hosts are online.
3. Check whether common TCP ports are open, such as 22, 80 or 443.
4. Display the results.

# Learning
The first step to creating this program would be to learn about sockets. Python's socket module allows us developers to attempt a TCP connection, but the succesfulness of the connection depends on the permissions of the device the program is running on and laws/policies. I found that the function .connect_ex() could be used to calculate whether the port was open or not (annotated). 0 is returned if the port is open, and anything else is returned if not.

# One time
By this point, we had a working program which is attempting a TCP connection on a socket it can find, checking if the port is open or not, and presenting the result. Next, I needed to get the program to scan a host. To do this, the main difference is that we check the most common ports using a for loop (for each in 22, 80, 443).

# Many times
Next, I need to adapt the program to be able to check many IP addresses. To do this, I can use python's ipaddress module, which allows us to retrieve all the addresses in a subnet. To do this we use the function .ip_network(). We can save the addresses we have as an array and pass through them in a neat for loop.

# Combining
Now that I can check all the IP addresses on a subnet for the selected, commonly opened ports using python's socket and ipaddress modules, I can combine my skills to create the full program, which will:
1. Find IP addresses on subnet.
2. For each host...
3. For each port in the commonly opened ports (22, 80, 443)...
4. Attempt a TCP connection.
5. Record results.