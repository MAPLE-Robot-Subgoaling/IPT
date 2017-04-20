
def main():

    currentHeight = int(input("Please enter the starting height of the hailstone: "))
    print("Hail is currently at height",(currentHeight))
    while currentHeight != 1:
        if (currentHeight % 2) == 0:
            print("Hail is currently at height", currentHeight / 2)
            currentHeight = (currentHeight / 2)
        elif (currentHeight % 2) == 1:
            print("Hail is currently at height", (currentHeight * 3) + 1)
            currentHeight = ((currentHeight * 3) + 1)
    print("Hail stopped at height 1")

main()
    
