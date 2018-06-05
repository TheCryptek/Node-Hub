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
                   
raw_input("Press enter to continue...")

# clear the screen once more
cryp.clear()




