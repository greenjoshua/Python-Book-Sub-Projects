def make_shirt(message, size = 'Large'):
    print("The shirt size is " + size.title() + " and the message printed on the shirt is '" + message + ".'")

make_shirt('I Love Python')
make_shirt(size = 's', message = 'I Love Python')
make_shirt(size = 'm', message = 'I Love Python')