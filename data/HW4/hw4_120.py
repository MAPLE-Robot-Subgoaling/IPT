def main():
    hailHeight = int(input("Please enter the starting height of the hailstone(in positive integer): "))
    while hailHeight != 1:
        if hailHeight % 2 == 0:
            hailHeight = hailHeight / 2
            print("Hail is currently at " , hailHeight)
        else:
            hailHeight = (hailHeight * 3) + 1
            print("Hail is currently at " , hailHeight)
    print( "Hail stopped at height " , hailHeight)
main()
