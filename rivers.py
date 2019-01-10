river = {'nile' : 'egypt' ,
         'illinois' : 'chicago' ,
         'ohio' : 'indianapolis',
         }

for river, city in river.items():
    print("The " + river.title() + " river runs through " + city.title() + ".")