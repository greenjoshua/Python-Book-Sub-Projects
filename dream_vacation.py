responses = {}

polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go?")

    responses[name] = response

    repeat = input("Would you like to let another person take the poll? (Yes/No)")
    if repeat == 'no':
        polling_active = False

print("\n--- Polliing Results ---")
for name, response in responses.items():
    print(name.title() + " wants to go to " + response.title())