def city_country(city, country):
    """Return a city and it's country."""
    return (city.title() + ", " + country.title())

city = city_country('hiedelberg' , 'germany')
print(city)

city = city_country('santiago' , 'chile')
print(city)

city = city_country('chicago' , 'united states')
print(city)