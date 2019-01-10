class User():
	"""A simple attempt to make a user profile."""
	def __init__(self, first_name, last_name, middle_name, age, major):
		self.first_name = first_name
		self.last_name = last_name
		self.middle_name = middle_name
		self.age = age
		self.major = major
		self.login_attempts = 0

	def describe_user(self):
		print("\nFirst name: " + self.first_name.title())
		print("Middle name: " + self.middle_name.title())
		print("Last name: " + self.last_name.title())
		print("Age: " + str(self.age))
		print("Major: " + self.major.title())

	def greet_user(self):
		print("\nHello " + self.first_name.title() + "," + "\nHow are you today?")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0
