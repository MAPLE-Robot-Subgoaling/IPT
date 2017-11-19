def main():
    startingHeight = int(input("Please enter the starting height of the hailstone:"))
    if  startingHeight != 1:
        while  startingHeight % 2 == 0:
            startingHeight = startingHeight / 2
            print ("Hail is currently at height",startingHeight)
        :
            startingHeight = ((startingHeight * 3)+1)/2
            print ("Hail is currently at height", startingHeight)
    else:
        print ("Hail stopped at height 1")
main()
