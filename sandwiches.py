def make_sandwiches(*toppings):
    print("\nNow making your sandwich with: ")
    for topping in toppings:
        print("-" + topping)

make_sandwiches('turkey' , 'cheese' , 'mustard')
make_sandwiches('extra roast beef')
make_sandwiches('pepperoni' , 'wheat bread' , 'provolone cheese' , 'mayonnaise')