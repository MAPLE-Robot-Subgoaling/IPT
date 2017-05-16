

def main():
	height = int(input("Enter the starting height of the hailstone:"))
	while height != 1:
		if (height % 2) == 0:
			height = height/2
			print("Hail is currently at height", height)
		else:
			height = (height*3) +1
			print("Hail is currently at height", height)		
	print("The hailstone has stopped at height", height)
main()
