def scale():
	feeling = input('How are you feeling today? (1-5)\n>>')
	feeling = int(feeling)
	if feeling < 1 or feeling > 5:
		print("Invalid input, enter a value 1 - 5")
		scale()
	elif feeling == " ":
		pass
	else:
		if feeling == 1:
			feeling = "Worse"
			message = "Hope you feel better soon :)"
		elif feeling == 2:
			feeling = "Bad"
			message = "It is not too late to turn it around"
		elif feeling == 3:
			feeling = "Ok"
			message = "There is potential!"
		elif feeling == 4:
			feeling = "Good"
			message = "Glad you are well!"
		else:
			feeling = "Best"
			message = "It is a great day!"
	return f'You are feeling {feeling}... \n\t{message}'

f = scale()
file = open("feelings-op.txt","w")
file.write("Feelings \n")
file.writelines(f)
file.close()