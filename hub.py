# -----------------------------------------------------
# --[ Project     : Node-Network
# --[ Part Name   : Node-Hub
# --[ description : A simple python backup script
# --[ author      : Brandon (TheCryptek) Conley
# --[ GitHub      : https://github.com/TheCryptek/Node-Hub
# --[ GitLab      : https://gitlab.com/TheCryptek/Node-Hub
# --[ Files       : cryp.py, hub.py
# --[ Version     : 0.1A
# -----------------------------------------------------

# Imports
import os
import sys
import zipfile
import traceback
import cryp
import platform
import socket

# Colors
header = cryp.bcolors.HEADER
blue = cryp.bcolors.OKBLUE
green = cryp.bcolors.OKGREEN
warning = cryp.bcolors.WARNING
fail = cryp.bcolors.FAIL
endc = cryp.bcolors.ENDC
bold = cryp.bcolors.BOLD
underline = cryp.bcolors.UNDERLINE

# Clear the terminal before the welcome screen
cryp.clear()

# The Welcome screen.
print header + """

 _   _           _        _   _      _                      _    
| \ | | ___   __| | ___  | \ | | ___| |___      _____  _ __| | __
|  \| |/ _ \ / _` |/ _ \ |  \| |/ _ \ __\ \ /\ / / _ \| '__| |/ /
| |\  | (_) | (_| |  __/ | |\  |  __/ |_ \ V  V / (_) | |  |   < 
|_| \_|\___/ \__,_|\___| |_| \_|\___|\__| \_/\_/ \___/|_|  |_|\_\
                                                                 
                     _   _       _     
                    | | | |_   _| |__  
                    | |_| | | | | '_ \ 
                    |  _  | |_| | |_) |
                    |_| |_|\__,_|_.__/ 
                    
          Created by Brandon (TheCryptek) Conley
""" + endc

# Print system info
print header + 'System: ' + endc + platform.system()
print header + 'Release: ' + endc + platform.release()

#add a space
cryp.space()
                   
raw_input("Press enter to continue...")

# clear the screen
cryp.clear()

# Node Network Hub Message
print warning + """
You are about to start Node Network Hub, this will make your machine the Hub
of a node network. Other nodes who have the IP of this hub will be able to
connect as long as you have your ports forwarded correctly! If you want
this machine to connect to an already existing Node Hub, then please use
Node Network Client.
""" + endc

# make sure they understand
print "Do you understand? Y/N"
answer = raw_input("> ")

# clear the screen
cryp.clear()

# What we do with their answer
if (answer == 'Y'):
    #while(True):
        class Server():
            def __init__(self,Address=('IP Address of Server',25565),MaxClient=2):
                
                self.s = socket.socket()
                self.s.bind(Address)
                self.s.listen(MaxClient)
            def WaitForConnection(self):
                
                self.Client, self.Adr=(self.s.accept())
                print('Got a connection from: '+str(self.Client)+'.')
            
        s = Server()
        s.WaitForConnection()
else:
    print "You said no"

