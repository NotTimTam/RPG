# Welcome to the shop.
import random, time, os, colorama, json
from colorama import init, Fore, Back, Style

# Skeleton animation.
skelly = """\n\n\n\n\n\n     ╔═══════════════════════════════════════════════════════════════════════════════════════╗\n     ║      _..--""---.                                                                      ║\n     ║     /           ".    *ZARGAR the SKELETON merchant bumbulingly skips into the room*  ║\n     ║     `            l                                                                    ║\n     ║     |'._  ,._ l/"     "Would you like to buy my wares? I have various wares for sale. ║\n     ║     |  _J<__/.v._/     You should definitely buy my wares."                           ║\n     ║      \\( ,~._,,,,-)                                                                    ║\n     ║       `-\\' \\`,,j|                                                                     ║\n     ║          \\_,____J                                                                     ║\n     ║     .--.__)--(                                                                        ║\n     ╚═══════════════════════════════════════════════════════════════════════════════════════╝"""

shop_items = {"Health Potion": 15, "Raspberry Cram": 50, "Berry Cram": 100, "Very Berry Cram": 200}

# Shop design and control.
class shop():
	# Begin shopping
	@staticmethod
	def go_shop():
		buying_his_wares = True
		print(skelly)

		# Check if the user wants to buy anything...
		while True:
			inp = input("     BUY HIS WARES? (y/n) ")
			if inp == "y" or inp == "Y" or inp == "yes" or inp == "YES" or inp == "Yes":
				buying_his_wares = True
				break
			elif inp == "n" or inp == "N" or inp == "no" or inp == "NO" or inp == "No":
				buying_his_wares = False
				break
			else:
				print("     '" + inp + "' isn't a valid input.\n     Try 'n' or 'y'!\n")
				continue

		if buying_his_wares == False:
			return "\n     *The SKELETON frowns and trudges away...*\n"
		else:
			print("\n     *The SKELETON smiles and opens his bag.*")

		# Wait a few seconds.
		time.sleep(2)

		# Display the shop.
		os.system('cls' if os.name == 'nt' else "printf '\033c'")

		shoplst = []
		for i in shop_items:
			shoplst.append(i + " | $" + str(shop_items[i]))

		consoleHeight = 20  # number of lines visible
		numEmptyLines = consoleHeight - len(shoplst)

		halfOfEmptyLines = ''

		for _ in range(0, (numEmptyLines // 2)):
		    halfOfEmptyLines += "\n"

		inventoryDisplay = '                              ╔══════════════════════════════════════╗\n                              ║              ' + \
		                   Fore.CYAN + ' - SHOP - ' + Fore.RESET + '              ║\n                              ║  ' \
		                                                              '                                    ║\n'
		for i in shoplst:
		    ilen = 36 - len(i)
		    inventoryDisplay += '                              ║ ' + i + (ilen * " ") + ' ║' + '\n'

		print(halfOfEmptyLines + inventoryDisplay + \
		       "                              ╚══════════════════════════════════════╝\n                                For help with the shop, type 'help'!\n")

		# Purchase System.
		while True:
			inp = input("                              > ")
			if inp == "help" or inp == "Help" or inp == "HELP":
				print("                              To buy an item, use this format: " + Fore.BLUE + "buy amount itemname." + Fore.RESET + "\n                              To sell an item, use this format: " + Fore.BLUE + "sell amount itemname." + Fore.RESET + "\n                              To re-observe items that are for sale, type " + Fore.BLUE + "'shop'" + Fore.RESET + ".\n                              To exit the shop at any time, type " + Fore.BLUE + "'done'" + Fore.RESET + ".")
			if inp == "shop":
				os.system('cls' if os.name == 'nt' else "printf '\033c'")

				shoplst = []
				for i in shop_items:
					shoplst.append(i + " | $" + str(shop_items[i]))

				consoleHeight = 20  # number of lines visible
				numEmptyLines = consoleHeight - len(shoplst)

				halfOfEmptyLines = ''

				for _ in range(0, (numEmptyLines // 2)):
				    halfOfEmptyLines += "\n"

				inventoryDisplay = '                              ╔══════════════════════════════════════╗\n                              ║              ' + \
				                   Fore.CYAN + ' - SHOP - ' + Fore.RESET + '              ║\n                              ║  ' \
				                                                              '                                    ║\n'
				for i in shoplst:
				    ilen = 36 - len(i)
				    inventoryDisplay += '                              ║ ' + i + (ilen * " ") + ' ║' + '\n'

				print(halfOfEmptyLines + inventoryDisplay + \
				       "                              ╚══════════════════════════════════════╝\n                                ")
			if inp == "done":
				break

			return '                              *The SKELETON closes his bag, thanks you for your purchase, and walks into the darkness...*'
