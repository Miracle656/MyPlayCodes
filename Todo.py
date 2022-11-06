'''def fibonacci_of(n):
	if n in {0, 1}:
		return n
	return fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case

num = int(input())

a = [fibonacci_of(n) for n in range(num)]

for i in a:
	print(i)'''




'''time = {}
for times in range(1,13):
    time[str(times)] = times + 12
	
	

cur_time = input()
cur_time = cur_time.split(":")

meridian = cur_time[1].split()

if "AM" in meridian:
    if int(cur_time[0]) > 9:
    	print(f"{cur_time[0]}:{meridian[0]}")
    else:
    	print(f"0{cur_time[0]}:{meridian[0]}")
elif "PM" in meridian:
	print(f"{time.get(cur_time[0])}:{meridian[0]}")'''








'''names = ["David", "John", "Annabelle", "Johnathan", "Veronica"]

#your code goes here

res = list(filter(lambda x: len(x) == 5, names))

print(res)'''



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
	







