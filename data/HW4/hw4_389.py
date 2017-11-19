def main():
    height = int(input("Please enter the starting height of the hailstone: "))
    while height != 1:
        print("Hail is currently at height", int(height))
        if height % 2 == 1:
            height = height * 3
            height += 1
        elif height % 2 == 0:
            height = height / 2
    print("Hail stopped at height", int(height))
main()
