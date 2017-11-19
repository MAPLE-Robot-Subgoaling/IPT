def main():
	userWidth = int(input("What is the width of your box? "))
	userHeight = int(input("What is the height of your box? "))
	userOutline = input("What is the symbol that you would like the box to be outlined in? ")
	userFiller = input("What is the symbol you would like the box to be filled in with? ")
	NO_BOX = 1
	if userWidth == NO_BOX and userHeight == NO_BOX:
		print (userOutline)
	else:
		print (userOutline * userWidth)
		for i in range (0, userHeight - 2):
			print (userOutline + (userFiller * (userWidth - 2)) + userOutline)
		print (userOutline * userWidth)
main()
