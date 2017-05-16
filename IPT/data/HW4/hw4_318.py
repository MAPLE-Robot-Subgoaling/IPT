
FINAL_HEIGHT = 1

def main():
	height = 0

	height = int(input("Enter the starting height of the hailstone: "))

	while height != FINAL_HEIGHT:
		print("Hail is currently at height", height)

		if height % 2 == 0:
			height = height // 2
		else:
			height = (height * 3) + 1

	print("Hail stopped at height", height)

main()
