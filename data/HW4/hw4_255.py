def main():
    initialHeight = int(input("Please enter the starting height of the hailstone: "))
    printStatement = "Hail is currently at height "
    print (printStatement + str(initialHeight))
    while(initialHeight != 1):
        if ((initialHeight % 2) == 0):
            initialHeight = initialHeight // 2
        elif ((initialHeight % 2 ) == 1):
            initialHeight = (initialHeight * 3) + 1
        if (initialHeight != 1):
             print (printStatement + str(initialHeight))
        else:
            print ("Hail stopped at height",  initialHeight)
main()
