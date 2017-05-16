
def main():
    END = 1
    NO_REMAINDER = 0
    height = int(input("Please enter the starting height of the hailstone: "))
    print("Hail is currently at height", height)
    while height != END:
        if height % 2 == NO_REMAINDER:
            height = height // 2
            if height == END:
                print("Hail stopped at height 1")
            else:
                print("Hail is currently at height", height)
        else:
            height = (height * 3) + 1
            print("Hail is currently at height", height)
main()
