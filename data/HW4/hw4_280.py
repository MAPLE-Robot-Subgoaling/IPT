def main():
    height = int(input("What is the current height of the hailstone? :"))
    while height != 1:
        print("The current height of the hailstone is ",height)
        if (height % 2) == 0:
            height = (height/2)
        elif (height % 2) == 1:
            height = (height * 3) + 1
    print("The current height of the hailstone is ", height)
main()
