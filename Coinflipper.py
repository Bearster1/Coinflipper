import random as rand
import colorama as col
import json

def read_save_data(savefile, slot):
	if savefile["new_file"][0]:
		print(f"{col.Fore.CYAN}{slot}{col.Style.RESET_ALL}. New File")
	else:
		print(f"File {col.Fore.CYAN}{slot}{col.Style.RESET_ALL}: ")
		for i in savefile:
			if savefile[i][1] != False:
				print(f"	{savefile[i][1]}{savefile[i][0]}")
def file_selection():
	print("Select a file: ")
	for j in range(3):
		read_save_data(file_data[j], j+1)
		print()

	print(f"Press {col.Fore.CYAN}4{col.Style.RESET_ALL} to delete a file.")
	print(f"Press {col.Fore.CYAN}5{col.Style.RESET_ALL} to duplicate a file.")
	print(f"Press {col.Fore.CYAN}6{col.Style.RESET_ALL} to rename a file.")
def randbool():
	oneOrZero = rand.randint(0,1)
	if oneOrZero == 1:
		return True
	else:
		return False
def headsOrTails():
	
	side = rand.randint(1,7)
	if side < 4:
		side = "Heads"
	elif side > 4:
		side = "Tails"
	elif side == 4:
		side = "Lucky"
	
	return side
def floatInput(message, lessthan, lowest = 0, lessthanmsg="You can only input an amount you already have"):
	while True:
		try:
			number = float(input(message))
		except:
			print("Please enter an float")
			continue
		if number > lessthan:
			print(lessthanmsg)
			continue
		if number <= lowest:
			print(f"You cannot bet {lowest} or lower.")
			continue
		break
	return number
def intInput(message):
	while True:
		try:
			number = int(input(message))
		except:
			print("Please enter an integer")
			continue
		if number > money:
			print("You can only bet an amount you already have")
			continue
		break
	return number
def boolInput(message, true, false):
	true = true.upper()
	false = false.upper()
	while True:
		bool = input(message).upper()

		if bool != true and bool != false:
			print(f"Please enter {col.Fore.CYAN}{true}{col.Style.RESET_ALL} or {col.Fore.CYAN}{false}{col.Style.RESET_ALL}")
			continue
		break
	return bool
def increaseLoan(num, amount = 1.1):
		num *= amount
		return roundToTwoDP(num)
def roundMoney(num):
		return roundToTwoDP(num)
def roundToTwoDP(number):
		list = str(float(number)).split(".")
		return float(list[0]+"."+list[1][:2])
def higherOrLowerInput(lowest, highest):
	while True:
		try:
			guess=int(input(f"Enter a number in the range {lowest}-{highest}: "))
			if guess <= lowest or guess >= highest:
				print("Number not in range.")
				continue
			break
		except:
			print("Please enter an integer")
	return guess
def minigame(money):
	print(f"{col.Fore.GREEN}Higher{col.Style.RESET_ALL} or {col.Fore.RED}Lower{col.Style.RESET_ALL}")
	print(f"Welcome to {col.Fore.GREEN}Higher{col.Style.RESET_ALL} or {col.Fore.RED}Lower{col.Style.RESET_ALL} a minigame where the goal is to guess the number then you will get that much back in {col.Fore.YELLOW}coins{col.Style.RESET_ALL}.")
	game_money=int(money)
	number = rand.randint(int(game_money/4+1),game_money*4-1)
	lowest=int(game_money/4)
	highest=game_money*4
	print(f"The range is {lowest}-{highest}")
	guess = None
	turns = 0
	while guess != number:
		turns+=1
		print(turns, end=". ")
		guess=higherOrLowerInput(lowest, highest)
		if guess > number:
			highest = guess
		elif guess < number:
			lowest = guess
		else:
			break
	print(f"You got the {col.Fore.GREEN}correct{col.Style.RESET_ALL} number!")
	print(f"You gain {col.Fore.YELLOW}{10-turns+number} coins{col.Style.RESET_ALL}.")
	return money+(10-turns+number)

while True:
	print(f"Welcome to {col.Fore.MAGENTA}Coinflipper{col.Style.RESET_ALL}")
	print()

	main_menu = False

	new_file_data = {
		"name": [None, "Name: "],
		"money": [10, "Money: "],
		"loan": [0, "Loan: "],
		"bank": [0, "Bank: "],
		"loan_time": [None, "Time Left On Loan: "],
		"day": [0, "Day: "],
		"prestige": [0, "Prestige Amount: "],
		"max_money": [0, False],
		"quickest_prestige": [None, False],
		"new_file": [True, False]
	}
	file_data = []
	for i in range(1, 4):
		try:
			file=open(f"coinflip_file_{i}.json", "x")
			json.dump(new_file_data, file, indent=4)
			file_data.append(new_file_data)
		except:
			file=open(f"coinflip_file_{i}.json", "r")
			file_data.append(json.load(file))
		file.close()

	file_selection()

	delete = False
	duplicate = False
	duplicate_from = None
	rename = False
	while True:
		chosen_file=input("")
		files = ["1", "2", "3"]
	
		if chosen_file == "4":
			print("Which file would you like to delete.")
			delete = True
			duplicate = False
			duplicate_from = None
			rename = False
			continue
	
		if chosen_file == "5":
			print("Which file would you like to duplicate.")
			delete = False
			duplicate = True
			duplicate_from = None
			rename = False
			continue

		if chosen_file == "6":
			print("Which file would you like to rename.")
			delete = False
			duplicate = False
			duplicate_from = False
			rename = True
			continue
	
		if chosen_file not in files:
			print("Please select a real file [{col.Fore.CYAN}1{col.Style.RESET_ALL}, {col.Fore.CYAN}2{col.Style.RESET_ALL}, {col.Fore.CYAN}3{col.Style.RESET_ALL}]: ")
			continue
		if delete:
			if file_data[int(chosen_file)-1]["new_file"][0]:
				print("You cannot delete a blank file.")
				print()
				file_selection()
				delete = False
				continue
			file=open(f"coinflip_file_{chosen_file}.json", "w")
			json.dump(new_file_data, file)
			file_data[int(chosen_file)-1]=new_file_data
			file.close()
			print("File deleted.")
			print()
			file_selection()
			delete = False
			continue

		if duplicate:
			if duplicate_from == None:
				if file_data[int(chosen_file)-1]["new_file"][0]:
					print("You cannot duplicate a blank file.")
					print()
					file_selection()
					duplicate = False
					continue

				duplicate_from = chosen_file
				print("Which file would you like to duplicate to.")
				continue
			
			file=open(f"coinflip_file_{chosen_file}.json", "w")
			json.dump(file_data[int(duplicate_from)-1], file)
			file_data[int(chosen_file)-1]=file_data[int(duplicate_from)-1]
			file.close()
			print("File duplicated.")
			print()
			file_selection()
			
			duplicate = False
			duplicate_from = None
			continue

		if rename:
			if file_data[int(chosen_file)-1]["new_file"][0]:
				print("You cannot rename a blank file.")
				print()
				file_selection()
				rename = False
				continue
			name = input("What would you like to rename the file to: ")
			file_data[int(chosen_file)-1]["name"][0] = name
			file=open(f"coinflip_file_{chosen_file}.json", "w")
			json.dump(file_data[int(chosen_file)-1], file)
			file.close()
			print("File renamed.")
			print()
			file_selection()
			rename = False
			continue
		break
	print(f"File {chosen_file} selected.")

	data = file_data[int(chosen_file)-1]

	if data["new_file"][0]:
		name = input("What would you like to name this file: ")
		data["name"][0] = name

	money = data["money"][0]
	loan = data["loan"][0]
	bank = data["bank"][0]
	loan_time = data["loan_time"][0]
	day = data["day"][0]
	prestige = data["prestige"][0]
	max_money = data["max_money"][0]
	quickest_prestige = data["quickest_prestige"][0]	
	
	while True:
		if money <= 0:
			print()
			print(f"You {col.Fore.RED}lost{col.Style.RESET_ALL} all your money. Here is a {col.Fore.RED}loan{col.Style.RESET_ALL} for {col.Fore.YELLOW}10 coins{col.Style.RESET_ALL} Use them wisely.")
			money += 10
			loan += 10
			if loan_time == None:
				loan_time=26
		print()

		loan_cost=110-0.5*(prestige)
		bank_cost=110+0.5*(prestige)
	
		if money>max_money:
			max_money=money
		day += 1
		print(col.Fore.MAGENTA+f"Day {day}:\n{col.Fore.YELLOW}Goal: {250*(prestige+1)+50*prestige} Coins{col.Style.RESET_ALL}")
		if loan_time != None:
			loan_time -= 1
			print(f"You have {col.Fore.RED}{loan_time} days{col.Style.RESET_ALL} left to pay your {col.Fore.RED}loan{col.Style.RESET_ALL}.")
	
		if day < 30:	
			if rand.randint(day, 30)==30:
				money=minigame(money)
	
		guess = boolInput(f"Heads [{col.Fore.CYAN}H{col.Style.RESET_ALL}] or Tails [{col.Fore.CYAN}T{col.Style.RESET_ALL}]: ", "H","T")
	
		bet = floatInput(f"How much would you like to bet (You have {col.Fore.YELLOW}{money} coins{col.Style.RESET_ALL}): ", money, 0.01)
	
		flip = headsOrTails()
		print(f"It was: {flip}")
	
		if guess == "T" and flip == "Tails":
			print(f"You are {col.Fore.GREEN}correct{col.Style.RESET_ALL}")
			money += bet
			money = roundMoney(money)
			print(f"You gained {col.Fore.YELLOW}{bet} coins{col.Style.RESET_ALL} now you have {col.Fore.YELLOW}{money} coins{col.Style.RESET_ALL}.")
		elif guess == "H" and flip == "Heads":
			print(f"You are {col.Fore.GREEN}correct{col.Style.RESET_ALL}")
			money += bet
			money = roundMoney(money)
			print(f"You gained {col.Fore.YELLOW}{bet} coins{col.Style.RESET_ALL} now you have {col.Fore.YELLOW}{money} coins{col.Style.RESET_ALL}.")
		elif flip == "Lucky":
			print(col.Fore.YELLOW+"You got lucky you got 5 times your bet"+col.Style.RESET_ALL)
			money += bet * 5
			money = roundMoney(money)
			print(f"You gained {col.Fore.YELLOW}{bet*5} coins{col.Style.RESET_ALL} now you have {col.Fore.YELLOW}{money} coins{col.Style.RESET_ALL}.")
		else:
			print(f"You are {col.Fore.RED}wrong{col.Style.RESET_ALL}")
			money -= bet
			money = roundMoney(money)
			print(f"You lost {col.Fore.YELLOW}{bet} coins{col.Style.RESET_ALL} now you have {col.Fore.YELLOW}{money} coins{col.Style.RESET_ALL}.")
	
		if loan != 0:
			payLoan = boolInput(f"Would you like to pay your {col.Fore.RED}loan{col.Style.RESET_ALL} of {col.Fore.YELLOW}{loan} coins{col.Style.RESET_ALL} [{col.Fore.CYAN}Y{col.Style.RESET_ALL}/{col.Fore.CYAN}N{col.Style.RESET_ALL}]: ", "Y", "N")
			if payLoan.upper() != "Y":
				loan = increaseLoan(loan, loan_cost/100)
				print(f"{col.Fore.RED}Loan{col.Style.RESET_ALL} increasing by {col.Fore.RED}{loan_cost-100}%{col.Style.RESET_ALL}, It is now at {loan}")
				
			elif money <= 10:
				print(f"If you try to pay a loan you will get to {col.Fore.YELLOW}0 coins{col.Style.RESET_ALL} so the loan hasn't been paid")
				loan = increaseLoan(loan, loan_cost/100)
				print(f"{col.Fore.RED}Loan{col.Style.RESET_ALL} increasing by {col.Fore.RED}{loan_cost-100}%{col.Style.RESET_ALL}, It is now at {loan}")
			elif money < loan:
				loan -= money
				money = 0
			
				money += 10
				loan += 10
			
				loan = roundMoney(loan)
			
				print(f"You don't have enough money to fully pay of the {col.Fore.RED}loan{col.Style.RESET_ALL} but we have shrunk it so you still have {col.Fore.YELLOW}10 coins{col.Style.RESET_ALL} but {col.Fore.YELLOW}{loan} coins{col.Style.RESET_ALL} in debt")
			
				loan = increaseLoan(loan, loan_cost/100)
				print(f"{col.Fore.RED}Loan{col.Style.RESET_ALL} increasing by {col.Fore.RED}{loan_cost-100}%{col.Style.RESET_ALL}, It is now at {loan}")
			elif money >= loan:
				money -= loan
				loan = 0
				money = roundMoney(money)
				print(f"You have {col.Fore.GREEN}paid{col.Style.RESET_ALL} of your loan and you have {col.Fore.YELLOW}{money} coins{col.Style.RESET_ALL} left.")
				loan_time = None
		
			if loan_time == 0:
				print(f"You have {col.Fore.RED}failed{col.Style.RESET_ALL} to pay your {col.Fore.RED}loan{col.Style.RESET_ALL}!")

				print(col.Fore.RED+"GAME OVER!")
				print(f"Final Score:\n{col.Fore.MAGENTA}Prestiges: {prestige}\n{col.Fore.YELLOW}Most money: {max_money}\n{col.Fore.MAGENTA}Quickest Prestige: {quickest_prestige} days\n{col.Fore.RED}Final Loan Cost: {loan}{col.Style.RESET_ALL}")
				print()
				print(f"Credits:")
				print("Creator: Bearster")
				print()
				print(f"Thank you for playing {col.Fore.MAGENTA}Coinflipper{col.Style.RESET_ALL}")
				print()
				input(f"Press {col.Fore.CYAN}enter{col.Style.RESET_ALL} to quit...")
				game=open(f"coinflip_file_{chosen_file}.json", "w")
				json.dump(new_file_data, game)
				game.close()
				break
					
			elif loan_time == 15 or loan_time == 5:
				loan = increaseLoan(loan, 2.5)
				print(f"You have {col.Fore.RED}{loan_time}{col.Style.RESET_ALL} days left until you will be kicked out if you do not pay of your {col.Fore.RED}loan{col.Style.RESET_ALL}. {col.Fore.RED}Loan{col.Style.RESET_ALL} increasing by {col.Fore.RED}150%{col.Style.RESET_ALL}, It is now at {col.Fore.YELLOW}{loan} coins{col.Style.RESET_ALL}.")
		
			elif loan_time == 20 or loan_time == 10:
				loan = increaseLoan(loan, 1.5)
				print(f"You have {col.Fore.RED}{loan_time}{col.Style.RESET_ALL} days left until you will be kicked out if you do not pay of your {col.Fore.RED}loan{col.Style.RESET_ALL}. {col.Fore.RED}Loan{col.Style.RESET_ALL} increasing by {col.Fore.RED}50%{col.Style.RESET_ALL}, It is now at {col.Fore.YELLOW}{loan} coins{col.Style.RESET_ALL}")
			
		if bank > 0:
			bank = increaseLoan(bank, bank_cost/100)
			bank = roundMoney(bank)
			print(f"Your account gained intrest. Your account now has {col.Fore.YELLOW}{bank} coins{col.Style.RESET_ALL}.")
		
		if day % 7 != 0:
			withdraw_insertbank = input(f"Would you like to withdraw your savings of {col.Fore.YELLOW}{bank} coins{col.Style.RESET_ALL} [{col.Fore.CYAN}W{col.Style.RESET_ALL}], insert your savings into your bank [{col.Fore.CYAN}I{col.Style.RESET_ALL}] or do neither [{col.Fore.CYAN}N{col.Style.RESET_ALL}]: ")
			if  withdraw_insertbank.upper() == "I":
				if money > 1:
					amount = floatInput(f"How much would you like to Insert (You have {col.Fore.YELLOW}{money} coins{col.Style.RESET_ALL}): ", money-1, 0, f"You cannot insert this much as you would be left with {col.Fore.YELLOW}0 coins{col.Style.RESET_ALL}.")
				
					amount = roundMoney(amount)
				
					money -= amount
					bank += amount
				
					money = roundMoney(money)
					bank = roundMoney(bank)
				
					print(f"Inserted {col.Fore.YELLOW}{amount} coins{col.Style.RESET_ALL} into your bank you now have {col.Fore.YELLOW}{money} coins{col.Style.RESET_ALL} and {col.Fore.YELLOW}{bank} coins{col.Style.RESET_ALL} in your bank")
				else:
					print("If I take your money then you wont have enough to bet!")
				
			elif withdraw_insertbank.upper() == "W":
				amount = floatInput(f"How much would you like to Withdraw (You have {col.Fore.YELLOW}{bank} coins{col.Style.RESET_ALL} in the bank): ", bank)
			
				amount = roundMoney(amount)
			
				bank -= amount
				money += amount
			
				money = roundMoney(money)
				bank = roundMoney(bank)
			
				print(f"Withdrew {col.Fore.YELLOW}{amount} coins{col.Style.RESET_ALL} from your bank you now have {col.Fore.YELLOW}{money} coins{col.Style.RESET_ALL} and {col.Fore.YELLOW}{bank} coins{col.Style.RESET_ALL} in your bank")
	
		if money >= 250*(prestige+1)+50*prestige:
			print()
			if quickest_prestige == None:
				quickest_prestige = day
			if day<quickest_prestige:
				print(f"This is your fastest {col.Fore.MAGENTA}prestige{col.Style.RESET_ALL} yet at {day} days.")
				quickest_prestige=day
			else:
				print(f"You {col.Fore.MAGENTA}prestiged{col.Style.RESET_ALL} in {day} days.")
			print(f"You got to {col.Fore.YELLOW}{250*(prestige+1)+50*prestige} coins{col.Style.RESET_ALL}! Now you will {col.Fore.MAGENTA}prestige{col.Style.RESET_ALL} and the goal will change to: {250*(prestige+2)+50*(prestige+1)}.)")
		
			loan = 0
			bank = 0
			loan_time = None
			day = 0
			prestige+=1
			money = 10+prestige*1.5
			print(f"Everything has reset. You now have {prestige} {col.Fore.MAGENTA}prestige{col.Style.RESET_ALL}. Bank intrest has increased to {110+0.5*(prestige)}%. Loan intrest has been decreased to {110-0.5*(prestige)}%.")
		print()
	
		print("Saving Game...")
	
		game=open(f"coinflip_file_{chosen_file}.json", "w")

		data["money"][0] = money
		data["loan"][0] = loan
		data["bank"][0] = bank
		data["loan_time"][0] = loan_time
		data["day"][0] = day
		data["prestige"][0] = prestige
		data["max_money"][0] = max_money
		data["quickest_prestige"][0] = quickest_prestige
		data["new_file"][0] = False
	
		json.dump(data, game)
		game.close()
	
		print()
	
		print("Would you like to quit: ")
		print(f"Press {col.Fore.CYAN}N{col.Style.RESET_ALL} to continue playing.\nPress {col.Fore.CYAN}Y{col.Style.RESET_ALL} to quit playing.\nPress {col.Fore.CYAN}M{col.Style.RESET_ALL} to return to the main menu.")
		exit = input("").upper()
		if exit == "Y":
			print(f"Thank you for playing {col.Fore.MAGENTA}Coinflipper{col.Style.RESET_ALL}")
			break
		if exit == "M":
			main_menu = True
			break
	if main_menu:
		continue
	break


