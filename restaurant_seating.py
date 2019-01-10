dining_group = input("Hi there, how many people will be dining with you tonight? ")
dining_group = int(dining_group)

if dining_group > 8:
    print("Ok, thank you. You'll have to wait for a table.")
else:
    print("Ok, thank you. Your table is ready!")
