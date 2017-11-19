def partFour():
    stoneHeight = int(input("What is the hailstone's height? \n"))
    while stoneHeight != 1:
        print("Current stone height: " + str(stoneHeight))
        if(stoneHeight % 2 == 0) :
            stoneHeight /= 2
        else:
            stoneHeight = stoneHeight * 3 +1
    print("Stone stopped at height: " + str(stoneHeight))
partFour()
