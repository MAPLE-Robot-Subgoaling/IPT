def main():
	width = int(input('Enter the width of the box: '))
	height = int(input('Enter the height of the box: '))
	symOut = input('Enter the symbol for the outline: ')
	symIn = input('Enter the symbol to fill in: ')
	line = ''
	Hrange = range(height)
	Wrange = range(width)
	for y in Hrange:
		if Hrange[y] == 0 or Hrange[y] == (height - 1):
			line = symOut * width
			print(line)
		else:
			line = ''
			for x in Wrange:
				if Wrange[x] == 0 or Wrange[x] == (width - 1):
					line = line + symOut
				else:
					line = line + symIn
			print(line)
main()
