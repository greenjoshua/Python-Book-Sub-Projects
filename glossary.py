from collections import OrderedDict

glossary = OrderedDict()

glossary["sorted"] = "lets you display your list in a particular order but doesn't affect the actual list."
glossary["remove"] = "deletes only the first occurrence of the value you specify."
glossary["pop"] = "removes the last item in a list, but lets you work with that item after removing it."
glossary["cd"] = "stands for change directory and is a used to navigate through your file system in a command window."
glossary["python interpreter"] = "reads through the program and determines what each word in the program means."
glossary["strings"] = "is simply a series of characters."


for word, definition in glossary.items():
    print("The " + word + " function " + definition)
