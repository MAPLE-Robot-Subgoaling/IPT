
def main():
    height = int(input("what is the starting height of the hailstone?"))
    while height != 1 and height % 2 == 0:
        height = height / 2
        print("the height is now", height)
        while height != 1 and height % 2 == 1:
            height = 3 * height + 1
            print("the height is now", height)
    print("The hail stopped at 1.")
main()
