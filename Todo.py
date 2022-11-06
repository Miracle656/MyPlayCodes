


print("========A Todo-List=======")
myList = []

if len(myList) == 0:
	print(f"Your List Item is empty: {myList}")

cont = 'y'

while cont == 'y':
	print('''\nWhat would you like to do
1. Add to list    2. Remove from list
3. Print list items\n''')
	choice = int(input("Select an option: "))
	if choice == 1:
		item = input("Enter the item name you want to add: ")
		if item in myList:
			print("Item already in list")
		else:
			myList.append(item)
	elif choice == 2:
		item = input("Enter the item name you want to remove: ")
		if item in myList:
			myList.remove(item)
		else:
			print("Item not found in list")
	elif choice == 3:
		print(f"standard view {myList}")
		print("List view below")
		count = 0
		for items in myList:
			count += 1
			print(f"{count}. {items}")
		
		
		
		
		
		
		
		
		

	cont = input("Would you like to do something else[y/n]: ")
	







