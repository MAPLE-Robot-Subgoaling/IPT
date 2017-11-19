def main():
    height = int(input("Please enter the starting height of the hailstone: "))
    while height != 1:
        if height == 1:
            print()
        elif height % 2 == 0:
            print("Hail is currently at height", height)
            height = height // 2
        else:
            print("Hail is currently at height", height)
            height *= 3
            height += 1
    print("Hail stopped at height", height)
main()
