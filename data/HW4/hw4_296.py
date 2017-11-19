def main():
    CUTOFF_HEIGHT = 1
    height = int(input("Please input a starting height for the hail: "))
    while height != CUTOFF_HEIGHT:
        print("The hailstone is currently at height:", int(height))
        if height % 2 == 0:
            height = height / 2
        else:
            height = (height * 3) + 1
    print("The hailstone stopped at", int(height))
main()
