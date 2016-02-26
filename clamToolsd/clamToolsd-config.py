#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# --------------------------------------------------------------
# Python Command-Line tools for clamav (clamToolsd-config)     |
# Created by clamsawd (clamsawd@openmailbox.org)               |
# Licensed by GPL v.3                                          |
# Last update: 26-02-2016                                      |
#                                                              |
# Dependences: ClamAV & Rsync (Optional)                       |
# Compatible with Python 3.x                                   |
# --------------------------------------------------------------
version="1.0"

#Import python-modules
import os
import sys

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
	os.chdir(os.environ["HOME"])
	print ("POSIX detected")
elif os.name == "nt":
	os.chdir(os.environ["USERPROFILE"])
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
	
#Create configuration of clamToolsd
ClearScreen()	
print ("")
print ("** clamToolsd (config) v"+version+" **")
print ("")
if os.name == "posix":
	print ("[RECOMMENDED] -> Type the path in single quotes.") 
	print ("[EXAMPLE] -> '/opt/example/'")
	print ("")
elif os.name == "nt":
	print ("[RECOMMENDED] -> Type the path in double quotes.")
	print ('[EXAMPLE] -> "C:\\Program Files"')
	print ("")
ForFtoScan=input("Type the folder(s) or file(s) to scan: ")
DayOfWeekInput=input("[Default: Sunday] Set Day of week (Monday(1), Tuesday(2), Wednesday(3), Thursday(4), Friday(5), Saturday(6), Sunday(7)): ")
if DayOfWeekInput == "1":
	DayOfWeek="1"
	NameOfDay="Monday"
elif DayOfWeekInput == "2":
	DayOfWeek="2"
	NameOfDay="Tuesday"
elif DayOfWeekInput == "3":
	DayOfWeek="3"
	NameOfDay="Wednesday"
elif DayOfWeekInput == "4":
	DayOfWeek="4"
	NameOfDay="Thursday"
elif DayOfWeekInput == "5":
	DayOfWeek="5"
	NameOfDay="Friday"
elif DayOfWeekInput == "6":
	DayOfWeek="6"
	NameOfDay="Saturday"
else:
	DayOfWeek="0"
	NameOfDay="Sunday"
TimeFormat=input("Type the time (HH:MM - 24h format): ")

#Show your configuration	
ClearScreen()
print ("")
print ("** clamToolsd (config) v"+version+" **")
print ("")
print ("Your configuration:")
print ("")
print ('Scan="'+ForFtoScan+'"')
print ('DayOfWeek="'+DayOfWeek+'"')
print ('NameOfDay="'+NameOfDay+'"')
print ('TheTime="'+TimeFormat+'"')
print ("")
PauseExit=input("+ Press ENTER to apply or Ctrl+C to cancel ")

#Apply configuration to 'clamToolsd.conf' file
abcf=open('clamToolsd.conf','w')
abcf.write('# sample configuration file of clamToolsd\n')
abcf.write('\n')
abcf.write('Scan="'+ForFtoScan+'"\n')
abcf.write('DayOfWeek="'+DayOfWeek+'"\n')
abcf.write('NameOfDay="'+NameOfDay+'"\n')
abcf.write('TheTime="'+TimeFormat+'"\n')
abcf.close()
