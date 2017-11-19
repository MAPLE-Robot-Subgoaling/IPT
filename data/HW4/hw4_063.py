def main():
    currHeight = int(input("Please enter the starting height for the hailstorm: "))
    newHeight = 1
    while currHeight > 1:
        newHeight = currHeight
        if newHeight % 2 == 0:
            newHeight = currHeight // 2
            print("Hail is currently",newHeight) 
        elif newHeight % 2 != 0:
            newHeight = (currHeight * 3) + 1
            print(" Hail is currently",newHeight)
    print("Hail stopped at",newHeight)
main()
