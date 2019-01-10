import unittest

from Employee import Employee

class TestEmployee(unittest.TestCase):
	"""Tests for the class Employee."""

	def setUp(self):
		"""
		Create an employee.
		"""
		self.james_dean = Employee('james', 'dean', 45000)

	def test_give_raise(self):
		self.james_dean.give_raise()
		self.assertEqual(self.james_dean.salary, 50000)

	def test_custom_give_raise(self):
		self.james_dean.give_raise(20000)
		self.assertEqual(self.james_dean.salary, 65000)