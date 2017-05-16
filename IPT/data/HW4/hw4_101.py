


def main():
    hailHeight = int(input("Enter the starting height of the hailstone: " ))

    print("Hail is at height" , int(hailHeight))

    while hailHeight != 2 :

        if hailHeight % 2 == 0:
            hailHeight = hailHeight / 2
            print("Hail is currently at height", int(hailHeight))


        elif hailHeight % 2 == 1:
            hailHeight = (hailHeight*3) + 1
            print("Hail is at height", int(hailHeight))
    print("Hail stopped at height 1")


        
        
main()
