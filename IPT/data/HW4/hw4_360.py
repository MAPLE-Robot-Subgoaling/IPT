
def main():


    hailHeight = int(input("Please enter the height of the hailstone: "))


    if hailHeight == 1:
        print("Hail stopped at height 1")

    while hailHeight > 1:

        
        modHail = hailHeight % 2


        if modHail == 0:
            hailHeight = hailHeight / 2
            print("Hail is currently at height", int(hailHeight))

            if hailHeight == 1:
                print("Hail stopped at height 1")


        elif modHail == 1:

            hailHeight = hailHeight * 3 + 1
            print("Hail is currently at height", int(hailHeight))


            if hailHeight == 1:
                print("Hail stopped at height 1")

main()
