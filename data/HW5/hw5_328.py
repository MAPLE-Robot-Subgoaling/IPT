def main():
	MIN_BOX = 1
	width = int(input("Please enter the width of the box: "))
	height = int(input("Please enter the height of the box: "))
	outline = input("Please enter a symbol for the box outline: ")
	fill = input("Please enter a symbol for the box fill: ")
	top_row = outline*width
	middle_row = outline+(fill*(width-2))+outline
	print(top_row)
	for i in range(height-2):
		print(middle_row)
	if height != MIN_BOX:
		print(top_row)
main()
