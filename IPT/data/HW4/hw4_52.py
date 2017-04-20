
def main ():

    startHeight= (int (input ("Please enter the starting height of the hailstone: ")))
    print ("Hail is currently at height", startHeight)


    while (int(startHeight) != 1):
        if (startHeight % 2 == 0):
            startHeight= (int (startHeight) // 2)
            print ("Hail is currently at height", startHeight)

        elif (startHeight % 2 == 1):
            startHeight= (startHeight * 3) + 1
            print ("Hail is currently at height", int(startHeight))
    
    if (int (startHeight) == 1):
        print ("Hail stopped at height 1")



main()
