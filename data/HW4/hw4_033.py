def main():
    height = int(input("Please enter the starting height of the hailstone: "))
    print("The height at start is ", height)
    while height != 1:
        if height%2 == 0:
            height = int(height/2)
            print("The height currently is ", height)
        elif height%2 != 0:
            height = int((height*3)+1)
            print("The height currently is ", height)
    print("The height at end is ", int(height))
main()
