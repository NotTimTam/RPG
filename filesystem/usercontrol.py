# Imports
import json
import os
import random
import colorama
from colorama import init, Fore, Back, Style

# Initialize colorama.
init()

"""Character Info Manipulation"""

# Health
def adjust_health(amount):
	# Open the data file.
	with open('./filesystem/save_data.json') as file:
		data = json.load(file)

	# Change the value.
	data['user_data']['health'] += amount

	# Save the new data.
	with open('./filesystem/save_data.json', 'w') as outfile:
		json.dump(data, outfile, indent=4)

# XP
def adjust_xp(amount):
	# Open the data file.
	with open('./filesystem/save_data.json') as file:
		data = json.load(file)

	# Change the value.
	data['user_data']['xp'] += amount

	# Save the new data.
	with open('./filesystem/save_data.json', 'w') as outfile:
		json.dump(data, outfile, indent=4)

# Level
def adjust_level(amount):
	# Open the data file.
	with open('./filesystem/save_data.json') as file:
		data = json.load(file)

	# Change the value.
	data['user_data']['level'] += amount

	# Save the new data.
	with open('./filesystem/save_data.json', 'w') as outfile:
		json.dump(data, outfile, indent=4)

# Luck
def adjust_luck(amount):
	# Open the data file.
	with open('./filesystem/save_data.json') as file:
		data = json.load(file)

	# Change the value.
	data['user_data']['luck'] += amount

	# Save the new data.
	with open('./filesystem/save_data.json', 'w') as outfile:
		json.dump(data, outfile, indent=4)

# Class
def adjust_luck(classname):
	# Open the data file.
	with open('./filesystem/save_data.json') as file:
		data = json.load(file)

	# Change the value.
	data['user_data']['class'] = classname

	# Save the new data.
	with open('./filesystem/save_data.json', 'w') as outfile:
		json.dump(data, outfile, indent=4)

# Add to Inventory
def add_to_inventory(itemname, itemamount):
	# Open the data file.
	with open('./filesystem/save_data.json') as file:
		data = json.load(file)

	if itemname in data['user_data']['inventory']:
		data['user_data']['inventory'][itemname] += itemamount
	else:
		data['user_data']['inventory'][itemname] = itemamount

	# Save the new data.
	with open('./filesystem/save_data.json', 'w') as outfile:
		json.dump(data, outfile, indent=4)

# Add to Weapons
def add_to_weapons(weaponname, level):
	# Open the data file.
	with open('./filesystem/save_data.json') as file:
		data = json.load(file)

	if weaponname in data['user_data']['weapons']:
		data['user_data']['weapons'][weaponname] += level
	else:
		data['user_data']['weapons'][weaponname] = level

	# Save the new data.
	with open('./filesystem/save_data.json', 'w') as outfile:
		json.dump(data, outfile, indent=4)

# Clean Inventory


"""Menu control functions."""

class functions():

    # Command help menu.
    @staticmethod
    def help():
        return '\n\n\n\n\n\n\n                                   ' \
               '╔══════════════════════════════╗\n                                   ║' + \
               (Fore.CYAN + '           - HELP -           ' + Fore.RESET) + \
               '║\n                                   ║ help: open this menu.        ║\n' \
               '                                   ║ clear: clear the screen.     ║\n' \
               '                                   ║ stats: get your stats.       ║\n                                   ║ inv: check your inventory.   ║\n                                   ║ wep: check your weapons.     ║                                   ' \
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
        name_format = name_format + (" " * (38 - name_length))

        # XP
        xp_format = ' XP: ' + str(xp)
        xp_length = len(xp_format)
        xp_format = xp_format + (" " * (38 - xp_length))

        # Level
        level_format = ' LVL: ' + str(level)
        level_length = len(level_format)
        level_format = level_format + (" " * (38 - level_length))

        # Health
        health_format = ' HP: ' + str(health)
        health_length = len(health_format)
        health_format = health_format + (" " * (38 - health_length))

        # Luck
        luck_format = ' LK: ' + str(luck)
        luck_length = len(luck_format)
        luck_format = luck_format + (" " * (38 - luck_length))

        # Class
        class_format = ' CLASS: ' + clss
        class_length = len(class_format)
        class_format = class_format + (" " * (38 - class_length))

        # Arrange and return the values in a fancy format.

        menusetup = ('\n\n\n\n\n\n\n\n                              '
                     '╔══════════════════════════════════════╗\n     '
                     '                         ║' + (
                             Fore.CYAN + '	              - STATS -              ' + Fore.RESET) + '║\n                              ║' + name_format + '║\n                              ║' + class_format + '║\n                              ║' + health_format + '║\n                              ║' + xp_format + '║\n                              ║' + level_format + '║\n                              ║' + luck_format + '║\n                              ╚══════════════════════════════════════╝\n\n')
        return menusetup

    # Command to give inventory.
    @staticmethod
    def inventory():
        """Grab inventory data"""

        # Open the data file.
        with open('./filesystem/save_data.json') as file:
            data = json.load(file)

        invlst = []
        for i in data['user_data']['inventory']:
            invlst.append(str(data['user_data']['inventory'][i]) + " | " + i)

        consoleHeight = 20  # number of lines visible
        numEmptyLines = consoleHeight - len(invlst)

        halfOfEmptyLines = ''
        for _ in range(0, (numEmptyLines // 2)):
            halfOfEmptyLines += "\n"

        inventoryDisplay = '                              ╔══════════════════════════════════════╗\n                              ║            ' + \
                           Fore.CYAN + ' - INVENTORY - ' + Fore.RESET + '           ║\n                              ║  ' \
                                                                      '                                    ║\n'
        for i in invlst:
            ilen = 36 - len(i)
            inventoryDisplay += '                              ║ ' + i + (ilen * " ") + ' ║' + '\n'

        return halfOfEmptyLines + inventoryDisplay + \
               '                              ╚══════════════════════════════════════╝'

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

        consoleHeight = 20  # number of lines visible
        numEmptyLines = consoleHeight - len(invlst)

        halfOfEmptyLines = ''
        for _ in range(0, (numEmptyLines // 2)):
            halfOfEmptyLines += "\n"

        inventoryDisplay = '                              ╔══════════════════════════════════════╗\n                              ║             ' + \
                           Fore.CYAN + ' - WEAPONS - ' + Fore.RESET + '            ║\n                              ║  ' \
                                                                      '                                    ║\n'
        for i in invlst:
            ilen = 36 - len(i)
            inventoryDisplay += '                              ║ ' + i + (ilen * " ") + ' ║' + '\n'

        return halfOfEmptyLines + inventoryDisplay + \
               '                              ╚══════════════════════════════════════╝'


# Command list...
commands = {'help': functions.help, 'clear': functions.clear, 'stats': functions.stats, 'inv': functions.inventory,
            'wep': functions.weapons}
