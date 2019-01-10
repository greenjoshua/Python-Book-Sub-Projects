def word_count(filename):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename, encoding='utf-8') as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		pass
	else:
		# Count the number of times a word appears in the file.
		num_words = contents.lower().count('the')
		print("'The' appears in " + filename + " " + str(num_words) + " times.")

filenames = ['trials_of_a_country_parson.txt', 'lollingdon_downs.txt']
for filename in filenames:
	word_count(filename)
