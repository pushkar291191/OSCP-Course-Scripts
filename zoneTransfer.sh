#!/bin/bash

# Simple Zone Transfer Bash Script

if [ -z "$1"]; then
		echo "[*] Simple Zone Transfer Script"
		echod "[*] Usage : $0 <domain name>"
		exit 0

fi

# If argument was given, identify the DNS servers for the domain.
# For each of these servers, attempt a zone transfer

for server in $(host -t ns $1 | cut -d " " -f4);do
	host -l $1 $server | grep "has address"

done