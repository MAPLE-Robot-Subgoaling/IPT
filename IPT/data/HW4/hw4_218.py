
def main():
    MIN_HEIGHT = 1

    height = int(input("Please enter the starting height of the hailstone: "))

    while (height > MIN_HEIGHT):
        print("Hail is currently at height", height)

        if (height % 2 == 0):
            height = height // 2
        else:
            height = height * 3 + 1

    print("Hail stopped at height", height)

main()
