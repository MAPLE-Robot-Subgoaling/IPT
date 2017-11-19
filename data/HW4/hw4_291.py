def main():
    height = int(input("Please enter the starting height of the hailstone: "))
    even = 0
    while height != 1:
        print("Hail is currently at height ", int(height))
        if (height % 2) == 0:
            height = height / 2
        elif (height % 2) != 0:
            height = (height * 3) + 1
    else:
        print("Hail stopped at height 1")
main()
