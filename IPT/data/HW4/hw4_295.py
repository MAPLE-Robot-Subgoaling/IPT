
def main():

    hailStoneHeight = int(input("Please enter the starting height of the hailstone: "))
    ODD = 1
    EVEN = 0

    print("Hail is currently at height", hailStoneHeight)

    while hailStoneHeight != ODD:  


        if hailStoneHeight % 2 == EVEN:

            hailStoneHeight = hailStoneHeight / 2
            if hailStoneHeight == ODD :
                print("Hail stopped at height", int(hailStoneHeight))
            else:
                print("Hail is currently at height", int(hailStoneHeight))

       

        elif  hailStoneHeight % 2 != EVEN:
            
            hailStoneHeight = (hailStoneHeight) * 3 + 1
            
            print("Hail is currently at height", int(hailStoneHeight))

main()
