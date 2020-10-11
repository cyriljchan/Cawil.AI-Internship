oprtn = ""
print("Hello! This is your friendly neighborhood simple calculator.")
while oprtn != "z":
	print("a. Addition")
	print("b. Subtraction")
	print("c. Multiplication")
	print("d. Division")
	print("e. Modulo")
	print("z. QUIT")
	oprtn = input("Please type the letter of the chosen operation. ")

	if oprtn != "z":
		x = int(input("Please input the first number. "))
		y = int(input("Please input the second number. "))
		if oprtn == "a":
			print("Answer is ", x+y)
		elif oprtn == "b":
			print("Answer is ", x-y)
		elif oprtn == "c":
			print("Answer is ", x*y)
		elif oprtn == "d":
			print("Answer is ", x/y)
		elif oprtn == "e":
			print("Answer is ", x%y)

		# elif oprtn == "e":
		# 	print("Answer is ", x%y)
		# elif oprtn == "e":
		# 	print("Answer is ", x%y)
		# elif oprtn == "e":
		# 	print("Answer is ", x%y)
		# elif oprtn == "e":
		# 	print("Answer is ", x%y)
		# elif oprtn == "e":
		# 	print("Answer is ", x%y)


	elif oprtn == "z":
		print("Thank you for using your friendly neighborhood simple calculator! Hope to see you again.")
	
	else:
		print("Please choose only from the above choices.")