
def main():
    print("The starting height for the hailstone should be a positive integer")
    hailstoneHeight = int(input("Please enter the starting height of the hailstone: "))
    while hailstoneHeight != 1:
        if (hailstoneHeight % 2 == 0):
            print("Hail is currently at height", hailstoneHeight / 2)
            hailstoneHeight = int(input("Please enter the starting height of the hailstone: "))
        else:
            print("Hail is currently at height", (hailstoneHeight * 3) + 1)
    
main()
        
        
