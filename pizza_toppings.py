# complete 7-4
prompt = "Enter your pizza toppings: "

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print("Adding " + topping + " to pizza.")