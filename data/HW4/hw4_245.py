def main():
    EVEN = 2
    height = int(float(input("Please enter the starting height of the hailstone: ")))
    print("Hail is currently at height",height)
    while height != 1:
        remainder = height % EVEN
        if remainder == 1:
            height = height * 3 + 1
            print("Hail is currently at height ",height)
            remainder = height % EVEN
        else:
            height = height / 2
            print("Hail is currently at height ",height)
            remainder = height % EVEN
    print("The hail stopped at 1.")
main()
