#fruit shop using function
fruit={}
cart_list=[]

def main_menu():
	print("....................Main menu..............................")
	print("1.Add Fruit")
	print("2.Delete Fruit by name")
	print("3.Search Fruit")
	print("4.Change Fruit Data and rate data")
	print("5.Display Details")
	print("6.Add to cart")
	print("7.Display cart")
	print("8.Exit")

def add_fruit():
	print(".............................Adding fruit...........................")
	fru_id = int(input("\tEnter the fruit id"))
	if fru_id not in fruit.keys():
		fru_name = input("\tEnter the name of the fruit")
		fru_rate = int(input("\tEnter the fruit rate"))
		fru_imported_from = input("\tImported from")
		fru_import_date = input("\tImported date")
		fru_buyed_price = int(input("\tEnter the price of the fruit"))
		temp ={
			"fruit_name":fru_name,
			"fruit_rate":fru_rate,
			"imported_from":fru_imported_from,
			"import_date":fru_import_date,
			"fruit_buyed_price":fru_buyed_price
		}
		fruit[fru_id] = temp
		print(fruit)
	else:
		print("fruit id is already taken")

def delete_fruit():
	print("..............................Deleting fruit......................")
	fru_id = int(input("\tEnter the fruit id"))
	name = input("\tEnter the name of the fruit")
	flag = False
	if fru_id in fruit.keys():
		for fru_del in fruit.values():
			print(fru_del['fruit_name'] == name)
			flag = True
	else:
		print("Invalid fruit id")
	if flag == True:
		del fruit[fru_id]
def search_fruit():
	print("..............................Searching fruit............................")
	print("1.search by name:")
	print("2.search by rate:")
	ch = int(input("\tEnter the choice"))
	if ch == 1:
		print(".............................searching fruit by name......................................")
		name = input("\tEnter the fruit name to be search")
		flag = False
		print("name",name)
		for i in fruit.values():
			if i["fruit_name"] == name:
				flag = True
				print("flag=>",flag)
			else:
				print("Invalid name")
		if flag == True:
			print(f"{i['fruit_name']} | {i['fruit_rate']} | {i['imported_from']} | {i['import_date']} | {i['fruit_buyed_price']}")
	elif ch == 2:
		print("....................................searching fruit by rate..................................")
		rate = int(input("\tEnter the fruit rate to be search"))
		flag = False
		for i in fruit.values():
			if i["fruit_rate"] == rate:
				flag = True
			else:
				print("\tInvalid raate")
		if flag == True:
			print(f"{i['fruit_name']} | {i['fruit_rate']} | {i['imported_from']} | {i['import_date']} | {i['fruit_buyed_price']}")

def change_fruit():
	print(".............................changing existing fruit details..........................")
	print("\t1.Change by name")
	print("\t2.Change by rate")
	ch1 = int(input("\tEnter the choice"))
	if ch1 == 1:
		print("...............................changing fruit name............................")
		fru_id = int(input("\tEnter the fruit id"))
		if fru_id not in fruit.keys():
			print("\tInvalid fruid id")
		else:
			new_name = input("\tEnter the new name")
			fruit[fru_id]['fruit_name'] = new_name
			print(fruit)
	if ch1 == 2:
		print(".................................changing fruit rate...............................")
		fru_id = int(input("\tEnter the fruit id"))
		if fru_id not in fruit.keys():
			print("\tInvalid fruit key")
		else:
			new_rate = int(input("\tEnter the new rate"))
			fruit[fru_id]['fruit_rate'] = new_rate
			print(fruit)

def display_fruit():
	print("..................................Displaying fruit details................................")
	for fid,fruits in fruit.items():
		print(f'{fid} | {fruits["fruit_name"]} | {fruits["fruit_rate"]} | {fruits["imported_from"]} | {fruits["import_date"]} | {fruits["fruit_buyed_price"]}')

def add_to_cart():
	print("........................Adding to cart..........................................")
	fru_id = int(input("\tEnter the fruit id"))
	if fru_id in fruit.keys():
		cart_list.append(fru_id)
		print(cart_list)

def display_cart():
	print(".......................Displaying cart.......................................")
	for i in cart_list:
		print(f"{i} | {fruit[i]}")


while True:
	main_menu()
	choice = int(input("\tEnter the choice"))
	if choice == 1:
		add_fruit()
	elif choice == 2:
		delete_fruit()	
	elif choice == 3:
		search_fruit()				
	elif choice == 4:
		change_fruit()
	elif choice == 5:
		display_fruit()
	
	elif choice == 6:
		add_to_cart()
	elif choice == 7:
		display_cart()
	elif choice == 8:
		break
	else:
		print("\tInvalid choice")

