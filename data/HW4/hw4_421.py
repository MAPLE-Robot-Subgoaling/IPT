def main():
	EVEN_OR_ODD_NUMBER = 2
	EVEN_HEIGHT = 0
	ODD_HEIGHT = 1
	HALF_HEIGHT = 2
	TIMES_3_HEIGHT = 3
	ONE_MORE_HEIGHT = 1
	HAILSTONE_STOP = 1
	currentHeight = int(input("Please enter the starting height of the hailstone: "))
	while currentHeight != 0:
		if (currentHeight % EVEN_OR_ODD_NUMBER) == EVEN_HEIGHT:
			currentHeight = (currentHeight / HALF_HEIGHT)
			print("The hail is currently at height: " + str(currentHeight))
		elif (currentHeight % EVEN_OR_ODD_NUMBER) == ODD_HEIGHT:
			currentHeight = (currentHeight * TIMES_3_HEIGHT) + ONE_MORE_HEIGHT
			print ("The hail is currently at height: " + str(currentHeight))
		if currentHeight == HAILSTONE_STOP:
			print("Hail stopped at height 1") 
			currentHeight = 0
main()
