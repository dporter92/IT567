#!/usr/bin/env python
from socket import *
import sys
import time
from optparse import OptionParser

#Variables
targetHost = ''
targetPort = ''
maxPortNum = 9999
minPortNum = 1
tp = []
th = []

#TCP Scanner function - opens up a connection and passes a 0 if the port is open
def myTCPscanner(targetHost, targetPort, code = 1):
	try:
		connection = socket(AF_INET, SOCK_STREAM) #SOCK_DGRAM - UDP
		connection.settimeout(2)
		myScannerCode = connection.connect_ex((targetHost, targetPort))
		if myScannerCode == 0:
			code = myScannerCode
		connection.close()
	except Exception, e:		
		pass
	return code
#My port range function - takes user input for the range and the command line targets and exits
def mpr(option, opt, value, parser):
	minPortNum = int(raw_input("Start Port: "))
	maxPortNum = int(raw_input("End Port: "))
	targetHost = parser.values.target
	th = []
	for j in targetHost.split(','):
		th += [j]

	print("Host(s): %s" % (th))
	print("\nPort scan started at %s" % (time.strftime("%H:%M:%S")))
	#Iterates through the hosts and then the ports using my TCP Scanner Function
	for hosts in th:
		print("\nHost: %s" % (hosts))
		for ports in range(minPortNum, maxPortNum):
			try:
				response = myTCPscanner(hosts, ports)

				if response == 0:
					print("Port %d: \tOPEN" % (ports))
			except Exception, e:
				pass
	print("\nPort scan finshed at %s" % (time.strftime("%H:%M:%S")))
	sys.exit()
#Command-line switches to specify host(s) and port(s)
parser = OptionParser()
parser.add_option("-t", "--target", help="target host address")
parser.add_option("-p", "--port", help="target port")
parser.add_option("-r", "--range", help="target port range", action="callback", callback=mpr)
(options, args) = parser.parse_args()
if not options.target:
	parser.error("Target host(s) not given (-t [Target Host],[Target Host])")
if not options.port:
	parser.error("Target port(s) not given (-p [Port Number],[Port Number]")

#Grab the hosts and ports from the command line switches
targetHost = options.target
targetPort = options.port

#Seperates the ports since they are added in a comma seperated list
for i in targetPort.split(','):
	tp += [int(i)]

#Seperates the hosts since they are added in a comma seperated list
for j in targetHost.split(','):
	th += [j]

#Start output
print("Host(s): %s \nPort(s): %s" % (th, tp))
print("\nPort scan started at %s" % (time.strftime("%H:%M:%S")))

#Iterate through every port indicated for each host and print if it is open or closed based on response
for hosts in th:
	print("\nHost: %s" % (hosts))
	for ports in tp:
		try:
			response = myTCPscanner(hosts, ports)
			if response == 0:
				print("Port %d/tcp: \tOPEN" % (ports))
			else:
				print("Port %d/tcp: \tCLOSED" % (ports))
		except Exception, e:
			pass

print("\nPort scan finshed at %s" % (time.strftime("%H:%M:%S")))
