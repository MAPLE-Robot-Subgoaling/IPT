def main():
	width = int(input("Please enter the width of the box: "))
	height = int(input("Please enter the height of the box: "))
	outerSymbol = input("Please enter a symbol for the box outline: ")
	fillSymbol = input("Please enter a symbol for the box fill: ")
	for h in range(height):
		if h == 0 or h == height - 1:
			s = outerSymbol
			s *= width
		else:
			s = outerSymbol + (fillSymbol * (width - 2)) + outerSymbol
		print(s)
main()
