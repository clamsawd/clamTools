#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# --------------------------------------------------------------
# python command-line tools for clamav (clamTools)             |
# Created by clamsawd (clamsawd@openmailbox.org)               |
# Licensed by GPL v.3                                          |
# Last update: 17-11-2015                                      |
#                                                              |
# Compatible with Python 3.x                                   |
# --------------------------------------------------------------
version=".unknown"

#Import python-modules
import subprocess
import os
import sys
import time

#Check if your system use Python 3.x
if sys.version_info<(3,0):
	print ("")
	print ("You need python 3.x to run this program.")
	print ("")
	exit()

#Function to clear screen
def ClearScreen():
	if sys.platform == "cygwin":
		print (300 * "\n")
	elif os.name == "posix":
		os.system("clear")
	elif os.name == "nt":
		os.system("cls")
	else:
		print ("Error: Unable clear screen")
					
#Detect system & PATH of user folder
if os.name == "posix":
	HomeUser=os.environ["HOME"]
	SystemUser="/"
	os.chdir(HomeUser)
	print ("POSIX detected")
elif os.name == "nt":
	HomeUser=os.environ["USERPROFILE"]
	SystemUser="C:"
	os.chdir(HomeUser)
	print ("Windows detected")

#Create clamTools folders
if not os.path.exists(".clamTools"):
	os.makedirs(".clamTools")
	os.chdir(".clamTools")
if os.path.exists(".clamTools"):
	os.chdir(".clamTools")
if not os.path.exists("db"):
	os.makedirs("db")
if not os.path.exists("logs"):
	os.makedirs("logs")
if not os.path.exists("qtn"):
	os.makedirs("qtn")
if not os.path.exists("pid"):
	os.makedirs("pid")
if not os.path.exists("tmp"):
	os.makedirs("tmp")

#Set variables of clamTools
if os.name == "posix":
	clamToolsdb=HomeUser+"/.clamTools/db/"
	clamToolslogs=HomeUser+"/.clamTools/logs/"
	clamToolsqtn=HomeUser+"/.clamTools/qtn/"
	clamToolspid=HomeUser+"/.clamTools/pid/"
	clamToolstmp=HomeUser+"/.clamTools/tmp/"
elif os.name == "nt":
	clamToolsdb=HomeUser+"\\.clamTools\\db\\"
	clamToolslogs=HomeUser+"\\.clamTools\\logs\\"
	clamToolsqtn=HomeUser+"\\.clamTools\\qtn\\"
	clamToolspid=HomeUser+"\\.clamTools\\pid\\"
	clamToolstmp=HomeUser+"\\.clamTools\\tmp\\"

#Check if exists 'freshclam.conf'
if os.path.isfile("freshclam.conf"):
	print ("freshclam.conf exists")
else:
	print ("freshclam.conf created")
	clamToolscf=open('freshclam.conf','w')
	clamToolscf.close()
	clamToolscf=open('freshclam.conf','a')
	clamToolscf.write('DatabaseOwner clamav\n')
	clamToolscf.write('UpdateLogFile '+clamToolslogs+'freshclam.log\n')
	clamToolscf.write('LogVerbose false\n')
	clamToolscf.write('LogSyslog false\n')
	clamToolscf.write('LogFacility LOG_LOCAL6\n')
	clamToolscf.write('LogFileMaxSize 0\n')
	clamToolscf.write('LogTime true\n')
	clamToolscf.write('SafeBrowsing Yes\n')
	clamToolscf.write('Foreground false\n')
	clamToolscf.write('Debug false\n')
	clamToolscf.write('MaxAttempts 5\n')
	clamToolscf.write('DatabaseDirectory '+clamToolsdb+'\n')
	clamToolscf.write('DNSDatabaseInfo current.cvd.clamav.net\n')
	clamToolscf.write('AllowSupplementaryGroups false\n')
	clamToolscf.write('PidFile '+clamToolspid+'freshclam.pid\n')
	clamToolscf.write('ConnectTimeout 30\n')
	clamToolscf.write('ReceiveTimeout 30\n')
	clamToolscf.write('TestDatabases yes\n')
	clamToolscf.write('ScriptedUpdates yes\n')
	clamToolscf.write('CompressLocalDatabase no\n')
	clamToolscf.write('Bytecode true\n')
	clamToolscf.write('Checks 24\n')
	clamToolscf.write('DatabaseMirror clamav.oucs.ox.ac.uk\n')
	clamToolscf.write('DatabaseMirror clamav.irontec.com\n')
	clamToolscf.write('DatabaseMirror db.local.clamav.net\n')
	clamToolscf.write('DatabaseMirror database.clamav.net\n')
	clamToolscf.close()
	
#Check if clamav is correctly installed
from subprocess import PIPE, Popen
try:
	clamscanCheck = Popen(['clamscan', '-V'], stdout=PIPE, stderr=PIPE)
	clamscanCheck.stderr.close()
	freshclamCheck = Popen(['freshclam', '-V'], stdout=PIPE, stderr=PIPE)
	freshclamCheck.stderr.close()
except:
	ClearScreen()
	print ("")
	print ("Error: 'clamav' is not installed!")
	print ("")
	print ("Help:")
	print ("  * http://www.clamav.net/downloads#sourcecode")
	print ("  * http://www.clamav.net/downloads#otherversions")
	print ("")
	PauseExit=input("Press ENTER to exit ")
	exit()

#Check parameters
try:
	if os.path.isfile(sys.argv[1]):
		ClearScreen()
		print ("")
		print ("- Running clamscan...")
		print ("- Loading virus database...")
		print ("")
		os.system("clamscan --follow-file-symlinks=0 -r '"+sys.argv[1]+"' --move="+clamToolsqtn+" --database="+clamToolsdb)
		print ("")
		PauseReturn=input("Press ENTER to return ")
		exit()
	elif os.path.exists(sys.argv[1]):
		ClearScreen()
		print ("")
		print ("- Running clamscan...")
		print ("- Loading virus database...")
		print ("")
		os.system("clamscan --follow-file-symlinks=0 -r '"+sys.argv[1]+"' --move="+clamToolsqtn+" --database="+clamToolsdb)
		print ("")
		PauseReturn=input("Press ENTER to return ")
		exit()
	else:
		print ("")
		print (sys.argv[1]+" doesn't exist")
		print ("")
except:
	print ("No parameters")
	
#Show main menu
MainMenu = 1
while MainMenu <= 2:
	ClearScreen()
	print ("")
	print (" - clamTools v"+version+" -")
	print ("")
	print ("   * Commands used: clamscan, freshclam")
	print ("   * Extra parameters: -r --follow-file-symlinks=0")
	print ("")
	print (" - Info -")
	print ("")
	print ("   * Quarantine: "+clamToolsqtn)
	print ("   * Logs: "+clamToolslogs)
	print ("   * Database: "+clamToolsdb)
	print ("")
	print (" - Options -")
	print ("")
	print ("   * (h) Home scan")
	print ("   * (c) Custom scan")
	print ("   * (s) System scan")
	print ("   * (u) Update")
	print ("   * (l) Log files")
	print ("   * (n) Quarantine")
	print ("   * (q) Quit")
	print ("")
	InputMenu=input(" - Choose an option: ")
 #Options from InputMenu variable
	if InputMenu == "h" or InputMenu == "H":
		ClearScreen()
		CurrentDate = time.strftime("%y-%m-%d")
		CurrentTime = time.strftime("%H-%M")
		print ("")
		print ("- Running clamscan...")
		print ("- Log file: "+clamToolslogs+"home-scan-["+CurrentDate+"]-["+CurrentTime+"].log")
		print ("- Loading virus database...")
		print ("")
		os.system("clamscan --follow-file-symlinks=0 -r '"+HomeUser+"' --move="+clamToolsqtn+" --database="+clamToolsdb+" --log="+clamToolslogs+"home-scan-["+CurrentDate+"]-["+CurrentTime+"].log")
		print ("")
		PauseReturn=input("Press ENTER to return ")
	elif InputMenu == "c" or InputMenu == "C":
		ClearScreen()
		print ("")
		ForFtoScan=input("Type the folder(s) or file(s) to scan: ")
		CurrentDate = time.strftime("%y-%m-%d")
		CurrentTime = time.strftime("%H-%M")
		print ("")
		print ("- Running clamscan...")
		print ("- Log file: "+clamToolslogs+"custom-scan-["+CurrentDate+"]-["+CurrentTime+"].log")
		print ("- Loading virus database...")
		print ("")
		os.system("clamscan --follow-file-symlinks=0 -r '"+ForFtoScan+"' --move="+clamToolsqtn+" --database="+clamToolsdb+" --log="+clamToolslogs+"custom-scan-["+CurrentDate+"]-["+CurrentTime+"].log")
		print ("")
		PauseReturn=input("Press ENTER to return ")
	elif InputMenu == "s" or InputMenu == "S":
		ClearScreen()
		CurrentDate = time.strftime("%y-%m-%d")
		CurrentTime = time.strftime("%H-%M")
		print ("")
		print ("- Running clamscan...")
		print ("- Log file: "+clamToolslogs+"system-scan-["+CurrentDate+"]-["+CurrentTime+"].log")
		print ("- Loading virus database...")
		print ("")
		os.system("clamscan --follow-file-symlinks=0 -r '"+SystemUser+"' --move="+clamToolsqtn+" --database="+clamToolsdb+" --log="+clamToolslogs+"system-scan-["+CurrentDate+"]-["+CurrentTime+"].log")
		print ("")
		PauseReturn=input("Press ENTER to return ")
	elif InputMenu == "u" or InputMenu == "U":
		ClearScreen()
		print ("")
		print ("- Updating virus database signatures....")
		print ("")
		os.system("freshclam --config-file=freshclam.conf")
		print ("")
		PauseReturn=input("Press ENTER to return ")
	elif InputMenu == "l" or InputMenu == "L":
		ClearScreen()
		print ("")
		print ("* List of log files ("+clamToolslogs+"):")
		print ("")
		if os.name == "posix":
			os.system("ls "+clamToolslogs+" | grep '.log'")
		elif os.name == "nt":
			os.system('dir /B '+clamToolslogs+' | find ".log"')
		print ("")
		PauseReturn=input("Press ENTER to return ")
	elif InputMenu == "n" or InputMenu == "N":
		ClearScreen()
		print ("")
		print ("* Quarantine ("+clamToolsqtn+"):")
		print ("")
		if os.name == "posix":
			os.system("ls -1 "+clamToolsqtn)
		elif os.name == "nt":
			os.system("dir /B "+clamToolsqtn)
		print ("")
		PauseReturn=input("Press ENTER to return ")
	elif InputMenu == "q" or InputMenu == "Q":
		print ("")
		print ("Exiting...")
		MainMenu += 2
	else:
		ClearScreen()
		print ("")
		print ("Invalid Option")
		print ("")
		PauseReturn=input("Press ENTER to return ")		
