print("Enter any two numbers and I'll add them for you.")
print("Enter 'q' to quit.")

while True:
	try:
		first_number = input('Enter first number: ')
		if first_number == 'q':
			break

		f_num = int(first_number)

		second_number = input('Enter second number: ')
		if second_number == 'q':
			break

		sec_num = int(second_number)

	except ValueError:
		print("Value entered is not an integer. Please input a number.")

	else:
		answer = f_num + sec_num
		print("The sum of " + str(f_num) + " and " + str(sec_num) + " is " +
		      str(answer) + ".")
