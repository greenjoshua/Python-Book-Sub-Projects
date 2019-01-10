def describe_city(city_name, country = 'united states'):
    print(city_name.title() + " is in " + country.title() + ".")

describe_city('michigan city')
describe_city('chicago')
describe_city(city_name = 'heidelber', country = 'germany')