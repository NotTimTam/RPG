# Run me to play the game!
from filesystem import setupuser as user
from filesystem import usercontrol
from filesystem.usercontrol import *
from filesystem.usercontrol import getstats as gt
import random, json, os

# Setup window...
cmd = 'mode 100,25'
os.system(cmd)

# Command dictionary.
commands = {'help': help, 'clear': clr, 'stats': usercontrol.getstats}

# Startup
user.startup()

# Main loop.
while True:
	inp = input("")
	try:
		if inp in commands:
			os.system('cls' if os.name == 'nt' else "printf '\033c'")
			print(commands[inp]())
			cmd = 'mode 100,25'
			os.system(cmd)
		else:
			raise Exception("\nI don't understand '" + inp + "'\nTry typing 'help' for some help...\n")
	except:
		print("\nI don't understand '" + inp + "'\nTry typing 'help' for some help...\n")
