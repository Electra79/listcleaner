#!/usr/bin/python3

###########################################
#Python wordlist cleaner for wpa/wpa2     #
#Currently only supports files in UTF-8   #
#    Braeden Orchard - February 2014      # 
###########################################

import sys
import os
import fileinput

defaultFolder = ("/usr/share/wordlists/listcleaner/")
defaultPath = ("/usr/share/wordlists/listcleaner/wpa.txt")

#Checks if the default folder exists
if not os.path.exists(defaultFolder):
    os.makedirs(defaultFolder)
#Checks if the default file exists (Give user option of making their own file)
try:
    check_file = open(defaultPath)
except IOError:
    check_file = open(defaultPath, "w")
check_file.close()
    
#Open the file to clean
print ("Specify the full path of the file you wish to clean")
fileToClean = input("> ")
with open(fileToClean) as FTC:
    with open(defaultPath, "a") as f:
        for line in FTC:
            if len(line) > 8:
                if len(line) < 35:
                    f.writelines(line)
