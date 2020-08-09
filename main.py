# Run me to play the game!
from filesystem import setupuser, usercontrol
import random, json, os

# Setup window...
cmd = 'mode 100,25'
os.system(cmd)

# Startup
setupuser.startup()

# Main loop.
while True:
	inp = input("> ")
	input_list = inp.split()
	usercontrol.clean_inv()
	usercontrol.round_health()
	try:
		if inp == "":
			pass
		elif inp == " ":
			pass
		elif input_list[0] in usercontrol.commands.keys():
			# Clear the screen and run the command.
			os.system('cls' if os.name == 'nt' else "printf '\033c'")
			#fn = getattr(usercontrol.functions, inp)
			fn = usercontrol.commands[inp]
			output = fn()
			print(output)
		elif input_list[0] == "consume":
			amount_str = input_list[1]
			amount = int(amount_str)
			if len(input_list) > 2:
				name_list = input_list[2:]
				name = ""
				for i in name_list:
					name += str(" " + i)
				name = name[1:]
			else:
				name = input_list[2]
			print(usercontrol.consume_items(name, amount))
		else:
			raise Exception("\nI don't understand '" + inp + "'\nTry typing 'help' for some help...\n")
	except Exception as e: print(e)
