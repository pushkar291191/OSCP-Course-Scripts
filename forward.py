
#!/usr/bin/python3

import subprocess
import os


### Allows code injection when used with hostile user input
# https://www.kevinlondon.com/2015/07/26/dangerous-python-functions.html

def openFile():
	domain = input ("Enter domain name  ")
	#The list.txt is copied from OSCP lab manual.  It has commonly used prefixes such as
	# www ftp mail owa proxy router admin www2 firewall mx pop3
	with open ("list.txt") as file:
		for line in file.readlines():
			name = line.strip()
			#print (name)
			bashCommand = "host " + name +"." + domain
			#print (bashCommand)
			try:
				output = callProcess (bashCommand)
				print (output.strip())
			except :
				pass

def callProcess(bashCommand):
	process = subprocess.check_output(bashCommand,shell = True)
	###############################
	#Convert the byte objesct into python before returning the result.
	return process.decode('utf-8')

if __name__ == '__main__':
	openFile() 



