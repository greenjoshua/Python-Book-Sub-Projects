# Exercise 7-8
sandwich_orders = ['peanut butter and jelly sandwich' , 'pastrami' , 'roast beef sandwich' , 'pastrami' , 'philly cheesesteak' ,
                   'pastrami']
finished_sandwiches = []

print("I'm sorry, but we've run out of Pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("Making your " + current_sandwich.title())

    finished_sandwiches.append(current_sandwich)


for sandwich in finished_sandwiches:
    print("Finished making your " + sandwich.title())