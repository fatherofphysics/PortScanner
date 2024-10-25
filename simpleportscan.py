#!/usr/bin/python3

import socket
import sys

usage = "python3 portscan.py IP StartPort(optional) EndPort(optional)"

if len(sys.argv) == 1:
	print(usage,file=sys.stderr)
	exit(1)

IP = sys.argv[1]
StartPort=1
EndPort=65535

if len(sys.argv) >= 3:
	StartPort=int(sys.argv[2])
	
	if len(sys.argv) >= 4:
		EndPort=int(sys.argv[3])


def check_port_stats(port:int) -> bool:
	try:
		s = socket.socket()
		s.settimeout(0.75)
		s.connect((IP,port))
		return True
	except (ConnectionRefusedError,socket.timeout):
		return False

for port in range(StartPort,EndPort+1):
	response = check_port_stats(port)

	if response:
		print(f"Port {port} is open")
