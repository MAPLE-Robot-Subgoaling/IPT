
def main():
    startHeight = int(input("Please enter the starting height of the hailstone: "))
    print("Hail is currently at height", startHeight)
        
    if startHeight == 1:
        print("Hail stopped at height 1")
    
    elif startHeight % 2 == 0:
        newHeight = startHeight // 2
        print("Hail is currently at height", newHeight) 
        while newHeight != 2:
            if newHeight % 2 == 1:
                newHeight = (newHeight * 3) +1
                print("Hail is currently at height", newHeight)
            elif newHeight % 2 == 0:
                newHeight = newHeight // 2
                print("Hail is currently at height", newHeight)
        print("Hail stopped at height 1")

    elif startHeight % 2 == 1:
        newHeight = (startHeight * 3) + 1
        print("Hail is currently at height", newHeight)
        while newHeight != 2:
            if newHeight % 2 == 1:
                newHeight = (newHeight * 3) + 1
                print("Hail is currently at height", newHeight)
            elif newHeight % 2 == 0:
                newHeight = newHeight // 2
                print("Hail is currently at height", newHeight)
        print("Hail stopped at height 1")
main()
