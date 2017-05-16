
def main():
	width = int(input('Please enter the width of the box: '))
	height = int(input('Please enter the height of the box: '))
	out = str(input('Please enter a symbol for the box outline: '))
	fill = str(input('Please enter a symbol for the box fill: '))

	exter = out * width
	inter = list(fill * width)
	inter[0] = inter[-1] = out
	inter = ''.join(inter)

	print(exter)
	for i in range(0, height-2):
		print(inter)
	print(exter)
main()
