def main():
    userHeight = int(input("Please enter a positive integer that will serve as the starting height for the hailstone: "))
    print("Hail height starts at", userHeight)
    while userHeight != 1:
        if userHeight % 2 == 1:
            userHeight = int((userHeight * 3) + 1)
            print("Hail height: " + str(userHeight))
        elif userHeight % 2 == 0:
            userHeight = int(userHeight / 2)
            print("Hail height: " + str(userHeight))
    if userHeight == 1:
        print("Hail has reached the height of 1!")
main()
