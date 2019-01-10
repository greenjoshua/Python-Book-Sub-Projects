class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		"""Make a class that resembles a restaurant."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print("The name of my restaurant is " + self.restaurant_name.title() + ".")
		print("They serve " + self.cuisine_type + ".")

	def open_restaurant(self):
		print(self.restaurant_name.title() + " is now open for business.")

	def set_number_served(self, number_served):
		self.number_served = number_served

	def increment_number_served(self, additional_served):
		self.number_served += additional_served

class IceCreamStand(Restaurant):
	"""Modeling an Ice cream stand based off of the Restaurant class."""
	def __init__(self, restaurant_name, cuisine_type = 'ice cream'):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = []

	def show_flavors(self):
		print("The restaurant has these flavors in stock: ")
		for flavor in self.flavors:
			print("\n- " + flavor)

the_big_one = IceCreamStand('the big one')
the_big_one.flavors = ['strawberry', 'chocolate', 'banana cream', 'almond joy']

the_big_one.show_flavors()
