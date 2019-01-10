#guest list of exercise 3-4 to 3-7 in chapter 3

guests = ['Kiley' , 'adam' , 'Tyler']
for guest in guests:
    message = "Hey, " + guest.title() + "!" + "\nI'm holding a dinner and you're invited."
    print(message)

message = guests[1].title() + " can't make it."
print(message)

guests.remove('adam')

guests.insert(1, 'Caitlyn')

for guest in guests:
    message = "Hey, " + guest.title() +"!" +  "\nI'm holding a dinner and you're invited."
    print(message)

update = "Just kidding, we have a bigger table. More people can come. Yay!!!!"

guests.insert(1, "Brandon")
guests.insert(0, "Aaron")
guests.append("Mason")

for guest in guests:
    message = "\nHey, " + guest.title() + "!" + "\nI'm holding a dinner and you're invited."
    print(update + message)

update = " I am so sorry, but I can now only invite two people to dinner and I have to un-invite you."
for guest in guests[2:]:
    if len(guests) >= 1:
        uninvited_guest = guests.pop()
        print("Hey, " + uninvited_guest +update)
    else:
        update = "\nI can now only have two people come to my dinner and you're still invited!!"
        print("Hey, " + guest.title() + update)

del guests[1]
del guests[0]
print(guests)



