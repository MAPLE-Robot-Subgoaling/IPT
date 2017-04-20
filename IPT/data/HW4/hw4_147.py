
def main():
    height = int(input("Please enter the starting height of the hailstone: "))
    print("Hail is currently at height", height)
    while height != 2 and height > 0:
        if height % 2:
            height = (height * 3) + 1
        else:
            height = height // 2
        print("Hail is currently at height", height)
    if height <= 0:
        print("Please enter a positive integer")
        main()
    if height > 0:
        print("The hail stopped at height 1")

main()
