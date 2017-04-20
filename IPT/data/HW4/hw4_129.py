
def main():
    
    stoneHeight = int(input("Please enter the height of the hailstone: "))

    while (stoneHeight > 1):
        
        print(stoneHeight)
        evenOrOdd = stoneHeight % 2

        if (evenOrOdd == 0):
            stoneHeight = stoneHeight // 2

        if (evenOrOdd == 1):
            stoneHeight = 1 + (stoneHeight * 3)
    
    print(stoneHeight)
    
main()
