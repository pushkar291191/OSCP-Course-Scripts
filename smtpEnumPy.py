#!/usr/bin/python3

import socket
import sys


def connectSMTP() :
	'''
	if len(sys.argv) != 2:
		print ("usage: smtpEnumpy.py <username>")
		sys.exit (0)
	'''

	with open ("users.txt","r") as file:
		names = file.read()
		#print (names)

	connectToSocket(names)
			
	'''	
		for line in file.readlines():

			name = line.strip()
			connectToSocket(name)
	'''
def connectToSocket(names):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	conenction = s.connect(('10.11.1.22',25))
	banner = s.recv(1024)	#To receive a response after connecting
	#print (banner)
	# VRFY command is used to verify an user. Check SMTP docs for more details
	name = names.split()

	for item in range(len(name)):		
		print ("Trying with user name {}".format(name[item]))
		command = 'VRFY ' + name[item] + '\r\n'
		#print ("the command is {}".format(command))
		nameEn = command		
		nameEn = command.encode()
		#print ('VRFY ' + nameEn+ '\r\n')
		#print (type(nameEn))
		s.send(nameEn)
		result = s.recv(1024)
		print ("The result is {}".format(result))

	s.close()


if __name__ == '__main__':
	connectSMTP()

