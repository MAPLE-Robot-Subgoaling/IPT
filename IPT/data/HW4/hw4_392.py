def main():
    hailStone = int(input("Please enter the starting height of the hailstone:"))
    print("Hail is currently at height", hailStone)
    while hailStone != 1:
        if hailStone % 2 == 0:
            hailStone = int(hailStone/2)
            print("Hail is currently at height", hailStone)
        else:
            hailStone = int((hailStone*3) + 1)
    print("Hail stopped at height", hailStone)
main()
