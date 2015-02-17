#!/usr/bin/python3

############################################
#   Python wordlist cleaner for wpa/wpa2   #
#   Currently only supports files in UTF-8 #
#       L Tumsi - February 2014            # 
############################################

import sys
import os
import fileinput

defaultFolder = ("/usr/share/wordlists/listcleaner/")
defaultPath = ("/usr/share/wordlists/listcleaner/wpa.txt")

#Checks if the default folder exists
def default_path():
    if not os.path.exists(defaultFolder):
        os.makedirs(defaultFolder)
        print("Default path doesn't exist, creating now...")

#Checks if the default file exists (Give user option of making their own file)
def file_check():
    try:
        check_file = open(defaultPath)
    except IOError:
        check_file = open(defaultPath, "a")
    check_file.close()

def banner():
    print("Hello and welcome to listcleaner! This script easily and quickly cleans up dictionary files by removing any words outside of the specified range.")
    print("Note that this script is still highly developmental and is likely to change drastically.")
    print("Please note that listcleaner currently only supports UTF-8 and treats comments like any other word.")
    print("You'll have to change format and remove comments manually")
    print("Questions? Comments? Email me at Ltumsi@gmail.com")

#Make the magic happen ;)
def main():
    #User specifies options
    print("Enter the path of the file you would like to clean: ")
    fileIn = input("> ")
    print("What is the minimum length you'd like to keep? Remember that WPA/WPA2 requires 8 characters")
    wordMin = int(input("> "))
    print("What is the maximum word length you'd like to keep? Remember that WPA/WPA2 requires 63 characters")
    wordMax = int(input("> "))
    wordMax = wordMax + 1
    wordMin = wordMin + 1
    with open(fileIn) as FTC:
        print("Would you like to write to your own file? Y/N")
        choice = input("> ")
        #If the user wants to specify their own path
        if choice.lower() == 'y':
            print("Enter the path of the file you wish to write to: ")
            userPath = input("> ")
            if not os.path.exists(userPath):
                os.makedirs(userPath)
                print("Creating path")
            print("Name your file")
            userFile = input("> ")
            try:
                checkFile = open(userFile)
            except IOError:
                print("Creating file")
                checkFile = open(userFile, "a+")
                print("Creating file")
            checkFile.close()
            userWrite = (""+userPath+""+userFile+"")
            print("Writing to: "+userPath+""+userFile+"")
            with open(userWrite, "a") as f:
                for line in FTC:
                    if len(line) > wordMin:
                        if len(line) < wordMax:
                            f.writelines(line)
        #Otherwise write to the default file
        else:
            defaultPath = ("/usr/share/wordlists/listcleaner/wpa.txt")
            print("Writing to: /usr/share/wordlists/listcleaner/wpa.txt")
            with open(defaultPath, "a") as f:
                for line in FTC:
                    if len(line) > wordMin:
                        if len(line) < wordMax:
                            f.writelines(line)
    #Gives user option to clean more than one file per session
    print("Finished writing. Would you like to clean another file? Y/N")
    restart = input("> ")
    if restart.lower() == 'y':
        main()
    else:
        print("Goodbye")
        sys.exit()

#Checks if the file exists before running main
default_path()
banner()
file_check()
main()
