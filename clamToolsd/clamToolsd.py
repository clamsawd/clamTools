#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# --------------------------------------------------------------
# python command-line tools for clamav (clamToolsd)            |
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
	exit(1)

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
	os.chdir(HomeUser)
	print ("POSIX detected")
elif os.name == "nt":
	HomeUser=os.environ["USERPROFILE"]
	os.chdir(HomeUser)
	print ("Windows detected")

#Create pclamTools folders
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

#Set variables of pclamTools
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

#Check if exists 'clamToolsd.conf'
if os.path.isfile("clamToolsd.conf"):
	print ("clamToolsd.conf exists")
	#Import variables from aria2bt.conf
	exec(open("clamToolsd.conf").read())
else:
	ClearScreen()
	print ("")
	print ("The configuration file doesn't exist")
	print ("")
	print ("You can create it if you run 'clamToolsd-config.py'")
	print ("")
	PauseReturn=input("Press ENTER to exit ")
	print ("Exiting...")
	exit()
	
#Run clamToolsd daemon
ClearScreen()
CurrentTime = time.strftime("%H:%M")
editlog=open(clamToolslogs+'clamToolsd.log','w')
print ("[clamToolsd] ["+CurrentTime+"] Initialized clamToolsd v"+version+" (Ctrl+C to stop)")
print ("[clamToolsd] ["+CurrentTime+"] Log in "+clamToolslogs+"clamToolsd.log")
print ("[clamToolsd] ["+CurrentTime+"] Scanning scheduled for day '"+NameOfDay+"' at "+TheTime+"h")
editlog.write("[clamToolsd] ["+CurrentTime+"] Initialized clamToolsd v"+version+"\n")
editlog.write("[clamToolsd] ["+CurrentTime+"] Scanning scheduled for day '"+NameOfDay+"' at "+TheTime+"h\n")
editlog.close()
time.sleep(3)

Scheduled = 1
while Scheduled <= 2:
	CurrentDay = time.strftime("%w")
	CurrentDate = time.strftime("%y-%m-%d")
	CurrentTime = time.strftime("%H:%M")
	if CurrentDay == DayOfWeek:
		if CurrentTime == TheTime:
			editlog=open(clamToolslogs+'clamToolsd.log','a')
			print ("[clamToolsd] ["+CurrentTime+"] Running clamscan...")
			editlog.write("[clamToolsd] ["+CurrentTime+"] Running clamscan...\n")
			print ("[clamToolsd] ["+CurrentTime+"] Log file: "+clamToolslogs+"daemon-scan-["+CurrentDate+"]-["+CurrentTime+"].log")
			editlog.write("[clamToolsd] ["+CurrentTime+"] Log file: "+clamToolslogs+"daemon-scan-["+CurrentDate+"]-["+CurrentTime+"].log\n")
			print ("[clamToolsd] ["+CurrentTime+"] Scanning "+Scan+"...")
			editlog.write("[clamToolsd] ["+CurrentTime+"] Scanning "+Scan+"...\n")
			os.system("clamscan --follow-file-symlinks=0 -r '"+Scan+"' --move="+clamToolsqtn+" --database="+clamToolsdb+" --log="+clamToolslogs+"daemon-scan-["+CurrentDate+"]-["+CurrentTime+"].log")
			print ("[clamToolsd] ["+CurrentTime+"] Next scheduled for day '"+NameOfDay+"' at "+TheTime+"h")
			editlog.write("[clamToolsd] ["+CurrentTime+"] Next scheduled for day '"+NameOfDay+"' at "+TheTime+"h\n")
			editlog.close()
			time.sleep(60)
	time.sleep(2)