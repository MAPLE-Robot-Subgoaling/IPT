def main():
    startingHeight = (int(input("Please enter the starting height of the hailstone:")))
    if (startingHeight == 1):
        print ("Hail stopped at height",startingHeight)
    else:
        print("Hail is currently at height",startingHeight)
    while (startingHeight != 1):
        if (startingHeight % 2) != 0:
            startingHeight = int(((startingHeight * 3) + 1))
            print("Hail is currently at height",startingHeight)
        if (startingHeight % 2) == 0:
            startingHeight = int((startingHeight / 2))
            if (startingHeight == 1):
                print ("Hail stopped at height",startingHeight)
            else:
                print("Hail is currently at height",startingHeight)
main()
