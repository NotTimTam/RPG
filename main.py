# Run me to play the game!
from filesystem import setupuser as user
from filesystem.usercontrol import *
from filesystem.usercontrol import getstats as gt
from filesystem.colorsystem import *
import random, time, json

# Command dictionary.
commands = {'help': help, 'clear': clr, 'stats': gt}

# Startup
user.startup()

# Main loop.
while True:
	inp = input("")
	try:
		if inp in commands:
			os.system('cls' if os.name == 'nt' else "printf '\033c'")
			print(commands[inp]())
		else:
			raise Exception("\nI don't understand '" + inp + "'\nTry typing 'help' for some help...\n")
	except:
		print("\nI don't understand '" + inp + "'\nTry typing 'help' for some help...\n")