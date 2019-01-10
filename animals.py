animals = ['cat' , 'dolphin' , 'dog' , 'rabbit' , 'squid' , 'bird' , 'seal' , 'rat']
for animal in animals:
    print("A " + animal + " would make an awesome pet!")
print("Actually, any of these animals would make an awesome pet!")

print("\nThe first three items in the list are:")
for animal in animals[:3]:
    print(animal.title())

print("\nThree items from the middle of the list are:")
for animal in animals[2:5]:
    print(animal.title())

print("\nThe last three items from the list are:")
for animal in animals[5:]:
    print(animal.title())