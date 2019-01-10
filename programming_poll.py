filename = 'programming_poll.txt'

print("Enter 'quit' when finished.")
while True:
	message = input("\nWhy do you like programming?")
	if message == 'quit':
		break
	else:
		with open(filename, 'a') as f:
			f.write(message + "\n")