

def main():

    hailHeight = int(input("Please enter the starting height of the hailstone: "))
    print("Hail is currently at height", hailHeight)

    while(hailHeight != 2 and hailHeight != 1):
        if((hailHeight % 2) == 0):
            hailHeight = hailHeight // 2  
        elif((hailHeight % 2) == 1):
            hailHeight = (hailHeight * 3) + 1
        print("Hail is currently at height", hailHeight)

    print("Hail stopped at height 1")

main()
