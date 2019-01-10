f_name = ['cats.txt', 'dogs.txt']
try:
	for filename in f_name:
		with open(filename) as f_obj:
			contents = f_obj.read()
			print(contents)
except FileNotFoundError:
	pass
