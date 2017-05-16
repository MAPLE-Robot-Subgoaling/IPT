def main():
    startingHeight = int(input("Input the starting height: "))
    currentHeight = startingHeight
    print(currentHeight)
    while currentHeight != 1:
        if( (currentHeight % 2) == 1):
            currentHeight = (currentHeight * 3) + 1
            print("The current height is",currentHeight)
        else:
            currentHeight = currentHeight//2
            print("The current height is",currentHeight)
    print("The hailstone has stopped at height",currentHeight,"! Finally.")
    

main()
