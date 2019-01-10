def city_country(city, country, population=''):
	"""Enter a city name and country name. Returns back in
	'city, country' format."""
	if population:
		return city.title() + ', ' + country.title() + ' - population ' + str(population)
	else:
		return city.title() + ', ' + country.title()

