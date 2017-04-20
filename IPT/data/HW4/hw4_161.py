

def main():


    startingHeight = int(input("Please enter the starting height of the hailstone:"))

    while startingHeight != 1 :
        if startingHeight % 2 == 0 :
            startingHeight = startingHeight / 2
        else :
            startingHeight = (startingHeight * 3) + 1
        print("Hail is currently at", startingHeight)
   
    print("Hail stopped at height", startingHeight)




main()


