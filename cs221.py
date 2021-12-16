def file_to_dictionary( path ):
	file = open(path , "r", encoding="utf8")

	text = file.read()
	text = text.lower()
	text = text.replace(",", "")
	text = text.replace(".", "")
	text = text.replace("?", "")
	text = text.replace(";", "")
	text = text.replace(":", "")
	text = text.replace("!", "")
	text = text.replace("%", "")

	words = []
	for sen in text.split("\n"):
		words+= sen.split(" ")

	dict_words = {}

	for w in words:
		if "_" in w :

			if not w in dict_words.keys():
				dict_words[w] = 1 
			else:
				dict_words[w] += 1

	
	return dict_words

def string_to_words( str ):
	str = str.lower()
	str = str.replace(",", " ")
	str = str.replace(".", " ")
	str = str.replace("?", " ")
	str = str.replace(";", " ")
	str = str.replace(":", " ")
	str = str.replace("!", " ")
	str = str.replace("%", " ")

	words = []

	for w in str.split(" "):
		if w != "":
			words.append( w )

	return words
