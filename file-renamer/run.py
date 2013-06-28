import os

for filename in os.listdir("."):
	filen = str(filename)
	l = len(filen)
	new = ""
	for letter in filen:
		if letter == " " or letter == ".":
			break
		else:
			new += letter
	os.rename(filename, new + ".jpg")


#	if filename.startswith("cheese_"):
#		os.rename(filename, filename[7:])
"""
> for each file loop through for statement
> convert filename to string
> store empty variable for new filename
> go through each letter in string using for statement
> store letter in empty variable and keep going
> if contains     then return new variable
> replace filename with new filename + .jpg"""