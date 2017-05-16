
def main():

    STOP = 1
    currentHeight = int(input("What is the height of the hailstone? "))
    
    while currentHeight > STOP:
        print("The hailstone is currently at height", currentHeight)
        modHeight = currentHeight % 2
        if modHeight == 1:
            newHeight = currentHeight * 3 + 1
        else:
            newHeight = currentHeight // 2
        currentHeight = newHeight

    print("Hail stopped at height 1.")

main()
