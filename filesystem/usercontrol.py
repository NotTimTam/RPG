# Imports
import json
import os
import random
import colorama
from colorama import init, Fore, Back, Style

init()

"""Menu control functions."""

# Command help menu.
def help():
	return '╔══════════════════════════════╗\n║' + (Fore.CYAN + '           - HELP -           ' + Fore.RESET) + '║\n║ help: open this menu.        ║\n║ clear: clear the screen.     ║\n║ stats: get your stats.       ║\n╚══════════════════════════════╝\n\n'

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

	# Formatted values.

	# Name
	name_format = ' NAME: ' + name
	name_length = len(name_format)
	name_format = name_format + (" " * (38-name_length))

	# XP
	xp_format = ' XP: ' + xp
	xp_length = len(xp_format)
	xp_format = xp_format + (" " * (38-xp_length))

	# Level
	level_format = ' LVL: ' + level
	level_length = len(level_format)
	level_format = level_format + (" " * (38-level_length))

	# Health
	health_format = ' HP: ' + health
	health_length = len(health_format)
	health_format = health_format + (" " * (38-health_length))

	# Luck
	luck_format = ' LK: ' + luck
	luck_length = len(luck_format)
	luck_format = luck_format + (" " * (38-luck_length))

	# Class
	class_format = ' CLASS: ' + clss
	class_length = len(class_format)
	class_format = class_format + (" " * (38-class_length))


	# Arrange and return the values in a fancy format.
	menusetup = ('╔══════════════════════════════════════╗\n║' + (Fore.CYAN + '               - STATS -              ' + Fore.RESET) + '║\n║' + name_format + '║\n║' + class_format + '║\n╚══════════════════════════════════════╝\n\n')
	return menusetup