


def main():

	boxWidth = int(input("Please enter the width of the box: "))
	boxHeight = int(input("Please enter the height of the box: "))
	boxOutline = str(input("Please enter a symbol for the box outline: "))
	boxFill = str(input("Please enter a symbol for the box fill: "))

	if boxHeight == 1 and boxWidth == 1 :
		print(boxOutline)
	elif boxHeight == 1 :
		print(boxOutline + boxFill*(boxWidth-2) + boxOutline)
	elif boxWidth == 1 :
		for n in range(0,boxHeight):
			print(boxOutline)
	else:
		print(boxOutline*boxWidth)
		for n in range(1,boxHeight-1):
			print(boxOutline + boxFill*(boxWidth-2) + boxOutline)
		print(boxOutline*boxWidth)

main()
