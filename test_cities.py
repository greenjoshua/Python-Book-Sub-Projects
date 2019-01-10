import unittest

from city_function import city_country

class CitiesTestCase(unittest.TestCase):
	"""Test for 'city_function.py' . """

	def test_city_country(self):
		"""Does a simple city, country pair work?"""
		santiago_chile = city_country('santiago', 'chile')
		self.assertEqual(santiago_chile, 'Santiago, Chile')

	def test_city_country_population(self):
		"""Does adding a population to the city, country pair work?"""
		santiago_chile_50000 = city_country('santiago', 'chile', population=50000)
		self.assertEqual(santiago_chile_50000, 'Santiago, Chile - population 50000')

if __name__ == '__main__':
	unittest.main()
