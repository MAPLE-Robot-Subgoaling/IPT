
def main():
    currentHeight = int(input("Please enter the starting height of the hailstone: "))
    while currentHeight != 1:
        print("The current height of the hailstone is", currentHeight)
        if currentHeight % 2 == 0:
            currentHeight = int(currentHeight / 2)
        elif currentHeight % 2 == 1:
            currentHeight = int((currentHeight * 3) + 1)
    print("The hailstone has stopped at 1")

main()
            
