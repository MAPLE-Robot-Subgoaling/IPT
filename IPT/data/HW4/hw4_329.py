
def main():
    
    hailstoneHeight = int(input("Input height of hailstone: "))
    
    while hailstoneHeight != 1:

        print("The hailstone is currently at height", hailstoneHeight)

        if hailstoneHeight % 2 == 0:
            hailstoneHeight = hailstoneHeight // 2

        elif hailstoneHeight % 2 == 1:
            hailstoneHeight = 3 * hailstoneHeight + 1
                
    print("The hailstone ends at height 1.")

main()
