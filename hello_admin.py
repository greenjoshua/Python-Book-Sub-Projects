usernames = ['mariah' , 'john' , 'sam' , 'adam' , 'admin']

if usernames:
	for user in usernames:
		if user == 'admin':
			print("Hello " + user.title() + ", would you like to see a status report?")
		else:
			print("Hello " + user.title() + ", how are you today?")
else:
	print("We need to find some users!")