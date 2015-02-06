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
def default_path():
    print("Default path doesn't exist, creating now...")
    if not os.path.exists(defaultFolder):
        os.makedirs(defaultFolder)

#Checks if the default file exists (Give user option of making their own file)
def file_check():
    try:
        check_file = open(defaultPath)
    except IOError:
        check_file = open(defaultPath, "w")
    check_file.close()

#Make the magic happen ;)
def main():
    print("Enter the path of the file you would like to clean: ")
    fileIn = input("> ")
    with open(fileIn) as FTC:
        print("Would you like to write to your own file? Y/N")
        defaultPath = input("> ")
        #If the user wants to specify their own path
        if defaultPath.lower() == 'y':
            print("Enter the path of the file you wish to write to: ")
            defaultPath = input("> ")
            file_check()
            print("Writing to: "+defaultPath+"")
            with open(defaultPath, "a") as f:
                for line in FTC:
                    if len(line) > 8:
                        if len(line) < 35:
                            f.writelines(line)
        #Otherwise write to the default file
        else:
            default_path()
            file_check()
            print("Writing to: /usr/share/wordlists/listcleaner/wpa.txt")
            with open(defaultPath, "a") as f:
                for line in FTC:
                    if len(line) > 8:
                        if len(line) < 35:
                            f.writelines(line)
    #Gives user option to clean more than one file per session
    print("Finished writing. Would you like to clean another file? Y/N")
    restart = input("> ")
    if restart.lower() == 'y':
        main()

#Checks if the file exists before running main
default_path()
main()
