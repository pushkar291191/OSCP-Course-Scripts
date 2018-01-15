#!/usr/bin/python3

import subprocess
import os


def hostProcess():
	domain = input ("Enter domain name  ")
	print ("The domain name is " .format(domain))
	bashCommand = "host -t ns " + domain
	process = subprocess.check_output(bashCommand,shell = True)
	#print (process)
	###############################	
	#Covert the byte object into strings
	stringProcess = process.decode("utf-8")
	print (stringProcess)
	#output = p1.communicate()[0]
	#print (output)


if __name__ == '__main__':
	hostProcess() 