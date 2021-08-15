#Fruit shop program using list
fruits=[]
while True:
	print(".................Main menu.......................")
	print("1.Add Fruit")
	print("2.Delete Fruit")
	print("3.Search Fruit")
	print("4.Change the fruit name and rate in the list")
	print("5.Display all fruit")
	print("6.exit")
	choice=int(input("Enter your choice"))
	if choice == 1:
		#Add Fruit
		print("...................Adding fruit...............")
		name=input("Enter the name of the fruit")
		rate=int(input("Enter the rate for the fruit"))
		if name:
			fruits.append([name,rate])
			print(fruits)

	elif choice == 2:
		#Delete Fruit
		print("............Deleting fruit.....................")
		print(fruits)
		name=input("Enter the name of the fruit to be deleted from the list")
		for i in fruits:
			if (fruits[fruits.index(i)][0] == name):
				fruits.pop(fruits.index(i))
		print(fruits)
	elif choice == 3:
		#Search Fruit by name and rate
		print(".........................search fruit....................")
		print(fruits)
		print("1.Search by name")
		print("2.Search by rate")
		choice1=int(input("Enter your choice"))
		if choice1 == 1:
			name1=input("Enter the name to search")
			for i in fruits:
				if (fruits[fruits.index(i)][0] == name):
					print(name1 + "name is in the list")
		elif choice1 == 2:
			rate=int(input("Enter the rate to be searched"))
			for i in fruits:
				if (fruits[fruits.index(i)][1]==rate):
					print("rate in the list")
	elif choice == 4:
		print(".................change fruit data.....................")
		#Change Fruit Data
		print("1.update name of the fruit list:")
		print("2.update rate of the fruit list:")
		choice2 = int(input("Enter the choice:"))
		if choice2 == 1:
			name=input("Enter the name to update :")
			new_name=input("Enter the new name :")
			for i in fruits:
				if (fruits[fruits.index(i)][0] == name):
					fruits[fruits.index(i)][0] = new_name
					print(fruits)
		elif choice2 == 2:
			rate=int(input("Enter the rate to update :"))
			new_rate=int(input("Enter the new rate :"))
			for i in fruits:
				if (fruits[fruits.index(i)][1] ==rate):
					fruits[fruits.index(i)][1] = new_rate
					print(fruits)
	
	elif choice == 5:
		print("..................Display data....................")
		#Display Fruits
		print(fruits)
		for i in range(0,len(fruits)):
			print(i+1,".",fruits[i])
	elif choice == 6:
		break
	else:
		print("invalid choice")
