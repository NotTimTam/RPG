# Run me to play the game!
from filesystem import setupuser as user
from filesystem import usercontrol
from filesystem.usercontrol import *
import random, json, os

# Setup window...
cmd = 'mode 100,25'
os.system(cmd)

# Startup
user.startup()

# Main loop.
while True:
	inp = input("")
	try:
		if inp in commands:
			# Clear the screen and run the command.
			os.system('cls' if os.name == 'nt' else "printf '\033c'")
			func = getattr(usercontrol.functions, inp)()
			print(func)
		else:
			raise Exception("\nI don't understand '" + inp + "'\nTry typing 'help' for some help...\n")
	except:
		print("\nI don't understand '" + inp + "'\nTry typing 'help' for some help...\n")
