# Imports
import random, json, os, colorama, time
from colorama import init, Fore, Back, Style

# Initialize colorama and window.
init()
cmd = 'mode 100,25'
os.system(cmd)
name = "rUNTIME pYTHON gAME"
os.system("title "+name)

# JSON
"""
with open('data.json') as file:
	data = json.load(file)
"""

# Check if data file exists.
try:
	file = open('./filesystem/save_data.json')
	print('\n\n\n\n\n\n\n\n\n\n                                  ╔═════════════════════════════╗\n                                  ║' + (Fore.RED + ' Found save data! Loading... ' + Fore.RESET) + '║\n                                  ╚═════════════════════════════╝')
except:
	print('╔══════════════════════════════╗\n║' + (Fore.GREEN + '    A NEW USER APPROACHES!    ' + Fore.RESET) + '║\n║' + (Fore.BLUE + ' Creating a save data file... ' + Fore.RESET) + '║\n╚══════════════════════════════╝')
	file = open('./filesystem/save_data.json', 'w')
	file.write('{}')
finally:
	file.close()

# Player information...

# Check if user data exists.
def check_for_user():
	# Open save data.
	with open('./filesystem/save_data.json') as file:
		data = json.load(file)
	# Check if the user_data content exists in the file.
	if 'user_data' in data:
		return True
	else:
		return False


# Create a user.
def create_user():
	# Make sure the user data doesn't exist before creating more.
	if check_for_user() == False:
		# Open save data.
		with open('./filesystem/save_data.json') as file:
			data = json.load(file)

		# Get the user's name.
		print('\n╔═══════════════════════════════╗\n║' + (Fore.MAGENTA + ' What is your name adventurer? ' + Fore.RESET) + '║\n╚═══════════════════════════════╝')
		name = input()
		data['user_data'] = {}
		if len(name) > 30:
			name = name[:30]
		data['user_data']['name'] = name

		# Add extra values the user can't control.
		data['user_data']['xp'] = 0
		data['user_data']['level'] = 1
		data['user_data']['health']=10
		data['user_data']['luck'] = 1

		# Get the user's class.
		print('\n╔═════════════════╗\n║' + (Fore.MAGENTA + ' Select a class! ' + Fore.RESET) + '║\n║ 1. Mage         ║\n║ 2. Knight       ║\n║ 3. Rogue        ║\n╚═════════════════╝')

		# Check that the user inputted a valid value for their class choice.
		inp = input("Type 1, 2, or 3: ")
		while True:
			if inp == '1':
				data['user_data']['class'] = "Mage"
				data['user_data']['inventory'] = {}
				data['user_data']['weapons'] = {}
				data['user_data']['inventory']['Coins'] = 5
				data['user_data']['weapons']['Staff'] = 1
				break
			elif inp == '2':
				data['user_data']['class'] = "Knight"
				data['user_data']['inventory'] = {}
				data['user_data']['weapons'] = {}
				data['user_data']['inventory']['Coins'] = 5
				data['user_data']['weapons']['Sword'] = 1
				break
			elif inp == '3':
				data['user_data']['class'] = "Rogue"
				data['user_data']['inventory'] = {}
				data['user_data']['weapons'] = {}
				data['user_data']['inventory']['Coins'] = 5
				data['user_data']['weapons']['Shortbow'] = 1
				break
			else:
				print("\nI don't understand '" + inp + "'")
				inp = input("\nTry typing 1, 2, or 3: ")

		# Save the new data
		with open('./filesystem/save_data.json', 'w') as outfile:
			json.dump(data, outfile, indent=4)

		# Finishing up.
		line = ' Starting ' + name + ' on their quest! '
		line_len = len(line)
		return '\n╔' + ("═" * line_len) + '╗\n║' + line + '║\n╚' + ("═" * line_len) + '╝'
	# Load user data since it already exists.
	else:
		return '\n╔══════════════════════╗\n║' + (Fore.MAGENTA + ' Loading user data... ' + Fore.RESET) + '║\n╚══════════════════════╝'

# Startup
def startup():
	version = (Fore.GREEN + 'Verson 0.2 Alpha' + Fore.RESET)
	nm = (Fore.RED + name + Fore.RESET)
	string = nm + " | " + version
	string_len = (len(string) + 2) - 20
	print("\n\n\n\n\n\n\n\n\n\n                            ╔" + (string_len*"═") + "╗\n                            ║ " + string + " ║\n                            ╚" + (string_len*"═") + "╝\n\n")
	time.sleep(2)

	# Loading screen...
	e = 100
	e2 = 10
	e3=0
	v=""
	while e > 0:
		os.system('cls' if os.name == 'nt' else "printf '\033c'")
		change = random.choice([1, 2, 3, 4, 5])
		#change = 100
		e -= change
		e2 += 1
		e3 += change
		if e2 > 7:
			e2 = 0
		if e2 == 0:
			v = "|"
		elif e2 == 1:
			v = "/"
		elif e2 == 2:
			v = "-"
		elif e2 == 3:
			v = "\\"
		elif e2 == 4:
			v = "|"
		elif e2 == 5:
			v = "/"
		elif e2 == 6:
			v = "-"
		elif e2 == 7:
			v = "\\"
		print("\n\n\n\n\n\n\n\n\n\n\n                                          " + (Fore.BLACK + Back.WHITE + (str(v) + Fore.RESET + Back.RESET) + (Fore.BLUE + " Loading... " + Fore.RESET) + str(e3) + "%"))
		time.sleep(0.01)

	os.system('cls' if os.name == 'nt' else "printf '\033c'")
	print("\n\n\n\n\n\n\n\n\n\n\n                                          " + (v + (Fore.GREEN + " Loaded!" + Fore.RESET)))
	time.sleep(0.5)
	os.system('cls' if os.name == 'nt' else "printf '\033c'")
	print("Welcome adventurer! Today's adventure is just on the horizon! What do we do first?")

# Run things...
create_user()
time.sleep(1)
os.system('cls' if os.name == 'nt' else "printf '\033c'")