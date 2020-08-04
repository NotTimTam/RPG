# Imports
import json
import os
import random
from filesystem.colorsystem import *

"""Menu control functions."""

# Command help menu.
def help():
	return f'╔══════════════════════════════╗\n║{bcolors.OKGREEN}           - HELP -           {bcolors.ENDC}║\n║ help: open this menu.        ║\n║ clear: clear the screen.     ║\n║ stats: get your stats.       ║\n╚══════════════════════════════╝\n\n'

# Clear screen.
def clr():
	os.system('cls' if os.name == 'nt' else "printf '\033c'")
	return ""

"""Player control functions"""

# Command to give stats.
def getstats():
	# Open the data file.
	with open('./filesystem/save_data.json') as file:
		data = json.load(file)

	# Grab all the values.
	name = data['user_data']['name']
	xp = data['user_data']['xp']
	level = data['user_data']['level']
	health = data['user_data']['health']
	luck = data['user_data']['luck']
	clss = data['user_data']['class']

	# Arrange and return the values in a fancy format.
	menusetup = (f'╔══════════════════════════════════╗\n║{bcolors.OKGREEN}             - STATS -            {bcolors.ENDC}║\n║ NAME: ' + name + '                        ║\n║ CLASS: ' + clss + '                     ║\n╚══════════════════════════════════╝\n\n')
	return menusetup