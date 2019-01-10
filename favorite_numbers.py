#fix numbers 6-10
favorite_numbers = {'kiley' : [7, 8, 9] ,
                    'jon' : [2, 4, 8] ,
                    'tevin' : [46, 81, 3] ,
                    'taylor' : [6, 72, 1] ,
                    'adam' : [5, 32, 10] ,
                    'james' : [25 , 60 , 7] ,
                    }

for name, numbers in favorite_numbers.items():
    print(name.title() + "'s favorite numbers are:")
    for number in numbers[:2]:
        print("\t" + str(number) + ",")
    for number in numbers[2:]:
        print("\t" + str(number) + ".")