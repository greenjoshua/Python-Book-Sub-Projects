def make_car(manufacturer, model, **car_profile):
    """Make a dictionary that contains information about a car."""
    profile = {}
    profile['manufacturer_name'] = manufacturer
    profile['model_name'] = model
    for key, value in car_profile.items():
        profile[key] = value
    return profile

car = make_car('honda', 'accord', color='blue' , tow_package=True)
print(car)