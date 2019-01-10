class Employee():
	"""A class to model an employee."""
	def __init__(self, first, last, salary):
		"""Initialize the employee."""
		self.first = first
		self.last = last
		self.salary = salary

	def give_raise(self, amount=5000):
		"""Give the employee a raise."""
		self.salary += amount