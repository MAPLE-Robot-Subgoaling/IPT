def main():
    height = int(input("Please enter a positive intiger for the starting height. "))
    print("The initial height of the hailstone was",height)
    while height != 1:
        while height % 2 == 0:
            height = height / 2
            print("The height of the hailstone is",height)
        while height % 2 == 1 and height != 1:
            height = (height * 3) + 1
            print("The height of the hailstone is",height)    
    print("The hailstone has hit the ground.")
main()
