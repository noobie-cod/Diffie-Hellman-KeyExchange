def chiper(txt,seed):
	txt = txt.split(" ")
	k = ""
	for word in txt:
		for letter in word:
			k = k + str(chr(ord(letter) + seed))
		k = k + str(" ")
	return (k.strip())


def dechiper(txt,seed):
	txt = txt.split(" ")
	k = ""
	for word in txt:
		for letter in word:
			k = k + str(chr(ord(letter) - seed))
		k = k + str(" ")
	return (k.strip())




