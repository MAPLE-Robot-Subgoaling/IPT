def main():
    height = int(input("Please enter the starting height as a positive integer: "))
    while height != 1:
        while height % 2 == 0:
            height = height / 2
            print("The current height is", height)
        while height % 2 == 1 and height != 1:
            height = (height * 3) + 1
            print("The current height is",height)
    if height == 1:
        print("The hailstone has hit the ground")
main()
