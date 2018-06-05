#   Author: Brandon (TheCryptek) Conley
#   This module is created for snippets
#   I use frequently in Python.

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
# Don't forget this is how to clear the terminal    
# cryp.clear()

def space():
    print " "
# Don't forget this is how to space
# cryp.space()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
# This is to help with colors in actual script
# header = cryp.bcolors.HEADER
# blue = cryp.bcolors.OKBLUE
# green = cryp.bcolors.OKGREEN
# warning = cryp.bcolors.WARNING
# fail = cryp.bcolors.FAIL
# endc = cryp.bcolors.ENDC
# bold = cryp.bcolors.BOLD
# underline = cryp.bcolors.UNDERLINE
