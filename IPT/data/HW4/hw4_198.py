
def main():

    hailstone = int(input("Please enter the starting height of the hailstone: "))
    while(hailstone != 1):
        if hailstone % 2 == 0:
            hailstone = int(hailstone / 2)
            print("Hail is currently at height", hailstone)
        else:
            hailstone = int(hailstone * 3 + 1)
            print("Hail is currently at height", hailstone)
                           


main()
