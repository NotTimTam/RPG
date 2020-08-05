# Imports
import json
import os
import random
import colorama
from colorama import init, Fore, Back, Style

# Initialize colorama.
init()

"""Menu control functions."""


class functions():

	# Command help menu.
	@staticmethod
	def help():
		return '\n\n\n\n\n\n\n                                   ' \
			'╔══════════════════════════════╗\n                                   ║' +\
			(Fore.CYAN + '           - HELP -           ' + Fore.RESET) + \
			'║\n                                   ║ help: open this menu.        ║\n'\
			'                                   ║ clear: clear the screen.     ║\n'\
			'                                   ║ stats: get your stats.       ║\n                                   ║ inv: check your inventory.   ║\n                                   ║ wep: check your weapons.     ║                                   '\
			'                                 ╚══════════════════════════════╝\n'

	# Clear screen.
	@staticmethod
	def clear():
		os.system('cls' if os.name == 'nt' else "printf '\033c'")
		return ""

	"""Player control functions"""

	# Command to give stats.
	@staticmethod
	def stats():
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
		xp_format = ' XP: ' + str(xp)
		xp_length = len(xp_format)
		xp_format = xp_format + (" " * (38-xp_length))

		# Level
		level_format = ' LVL: ' + str(level)
		level_length = len(level_format)
		level_format = level_format + (" " * (38-level_length))

		# Health
		health_format = ' HP: ' + str(health)
		health_length = len(health_format)
		health_format = health_format + (" " * (38-health_length))

		# Luck
		luck_format = ' LK: ' + str(luck)
		luck_length = len(luck_format)
		luck_format = luck_format + (" " * (38-luck_length))

		# Class
		class_format = ' CLASS: ' + clss
		class_length = len(class_format)
		class_format = class_format + (" " * (38-class_length))


		# Arrange and return the values in a fancy format.

		menusetup = ('\n\n\n\n\n\n\n\n                              '
					 '╔══════════════════════════════════════╗\n     '
					 '                         ║' + (Fore.CYAN + '	              - STATS -              ' + Fore.RESET) + '║\n                              ║' + name_format + '║\n                              ║' + class_format + '║\n                              ║' + health_format + '║\n                              ║' + xp_format + '║\n                              ║' + level_format + '║\n                              ║' + luck_format + '║\n                              ╚══════════════════════════════════════╝\n\n')
		return menusetup

	# Command to give inventory.
	@staticmethod
	def inventory():
		print('\n\n\n\n\n\n\n\n                              ╔══════════════════════════════════════╗\n                              ║            ' + Fore.CYAN + ' - INVENTORY - ' + Fore.RESET + '           ║\n                              ║                                      ║')

		"""Grab inventory data"""

		# Open the data file.
		with open('./filesystem/save_data.json') as file:
			data = json.load(file)

		invlst = []
		for i in data['user_data']['inventory']:
			invlst.append(str(data['user_data']['inventory'][i]) + " | " + i)

		for i in invlst:
			ilen = 36 - len(i)
			print('                              ║ ' + i + (ilen * " ") + ' ║')

		return '                              ╚══════════════════════════════════════╝'

	# Command to give weapons.
	@staticmethod
	def weapons():
		"""Grab inventory data"""

		# Open the data file.
		with open('./filesystem/save_data.json') as file:
			data = json.load(file)

		invlst = []
		for i in data['user_data']['weapons']:
			invlst.append(i + " | Level: " + str(data['user_data']['weapons'][i]))

		middle = ((len(invlst) + 3) / 2)

		print('\n\n\n\n\n\n\n\n                              ╔══════════════════════════════════════╗\n                              ║             ' + Fore.CYAN + ' - WEAPONS - ' + Fore.RESET + '            ║\n                              ║                                      ║')

		for i in invlst:
			ilen = 36 - len(i)
			print('                              ║ ' + i + (ilen * " ") + ' ║')

		return '                              ╚══════════════════════════════════════╝'

# Command list...
commands = {'help': functions.help, 'clear': functions.clear, 'stats': functions.stats, 'inv': functions.inventory, 'wep': functions.weapons}
