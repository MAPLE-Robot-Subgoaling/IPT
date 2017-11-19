def main():
	STOP_HEIGHT = 1
	height = int(input("Please enter the starting height of the hailstone: "))
	while height != STOP_HEIGHT:
		print("Hail is currently at height", height)
		if height % 2 == 0:
			height //= 2
		else:
			height *= 3
			height += 1
	print("Hail stopped at height", STOP_HEIGHT)
main()
