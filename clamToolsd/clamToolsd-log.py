#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# --------------------------------------------------------------
# Python Command-Line tools for clamav (clamToolsd-log)        |
# Created by clamsawd (clamsawd@openmailbox.org)               |
# Licensed by GPL v.3                                          |
# Last update: 04-12-2015                                      |
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
	HomeUser=os.environ["HOME"]
	os.chdir(HomeUser)
	print ("POSIX detected")
elif os.name == "nt":
	HomeUser=os.environ["USERPROFILE"]
	os.chdir(HomeUser)
	print ("Windows detected")

#Create clamTools folders
if not os.path.exists(".clamTools"):
	os.makedirs(".clamTools")
	os.chdir(".clamTools")
if os.path.exists(".clamTools"):
	os.chdir(".clamTools")
if not os.path.exists("logs"):
	os.makedirs("logs")
	os.chdir("logs")
if os.path.exists("logs"):
	os.chdir("logs")

#See the log file
if os.path.isfile("clamToolsd.log"):
	print ("clamToolsd.log exists")
	ClearScreen()
	readfile=open('clamToolsd.log', 'r')
	print(readfile.read())
	readfile.close()
else:
	ClearScreen()
	print ("")
	print ("* clamToolsd.log doesn't exist.")
	print ("")
