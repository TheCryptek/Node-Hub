#   Author: Brandon (TheCryptek) Conley
#   This module is created for snippets
#   I use frequently in Python.

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def space():
    print " "

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
