

def main():
	starting_height = int(input("Please enter the starting height of the hailstone: "))
	print("Hail is currently at height",starting_height)
	while starting_height != 1:
		if starting_height % 2 == 0:
			starting_height = int(starting_height / 2)
			if starting_height != 1:
				print("Hail is currently at height",starting_height)

		else:
			starting_height = int((starting_height * 3) +1)
			if starting_height != 1:
				print("Hail is currently at height",starting_height)
	print("Hail is stopped at",starting_height)

main()
