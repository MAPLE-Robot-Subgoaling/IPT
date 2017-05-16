
def main ():

	width = int (input ("Please enter the width of the box: "))
	height = int (input ("Please enter the height of the box: "))
	outline = input ("Please enter a symbol for the box outline: ")
	inside = input ("Please enter a symbol for the box filling: ")

	topAndBottom = outline * width

	middle = outline + inside * (width - 2) + outline

	print (topAndBottom)

	for i in range (height - 2):
		print (middle)
	
	if height > 1:
		print (topAndBottom)

	print ("Thank you for using my code :) ")


main ()	