import json

def get_favorite_number():
	"""Display favorite number."""
	filename = 'favorite_number.json'
	try:
		with open(filename) as f_obj:
			favorite_number = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return favorite_number

def new_number():
	favorite_number = input("What is your favorite number?")
	filename = 'favorite_number.json'
	with open(filename, 'w') as f_obj:
		json.dump(favorite_number, f_obj)
	return favorite_number

def enter_new_number():
	"""Input a new favorite number."""
	favorite_number = get_favorite_number()
	if favorite_number:
		print("I know your favorite number! It's " + favorite_number + "!")
	else:
		favorite_number = new_number()
		print("Ok, so your favorite number is " + str(favorite_number) + "!")

enter_new_number()
