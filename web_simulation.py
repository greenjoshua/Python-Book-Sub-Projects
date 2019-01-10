current_users = ['kiley' , 'adam' , 'luke' , 'taylor' , 'jo']

new_users = ['james' , 'Kiley' , 'sam' , 'mike' , 'matt']

for user in new_users:
	if user.lower() in current_users:
		print("User name already taken. Please enter a different user name.")
	else:
		print("Username is available.")