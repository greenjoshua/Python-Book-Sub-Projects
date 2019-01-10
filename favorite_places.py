favorite_places = {'kiley' : ['italy' , 'greece' , 'germany'] ,
                   'adam' : ['china' , 'japan' , 'korea'] ,
                   'taylor' : ['florida' , 'malasia' , 'ireland']
                   }

for people, places in favorite_places.items():
    print(people.title() + "'s favorite places are:")
    for place in places:
        print("\t" + place.title())