



def main():

    initialHeight = int(input("Please enter the starting height of the hailstone: "))
    
    while initialHeight != 1:
        if initialHeight % 2 == 0:
            print("Hail is currently at height " , initialHeight)
            initialHeight = int(initialHeight/2)
        elif initialHeight % 2 == 1:
            print("Hail is currently at height " , initialHeight)
            initialHeight = int((initialHeight * 3) + 1)

    print("Hail stopped at height 1.")



main()
