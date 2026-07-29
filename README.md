# Socket-Scanner
This program takes an IP address of a subnet, tries to determine which hosts are online, checks whether common TCP ports are open and displays the results.

# Cyber Information
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