
def main():

    END_HEIGHT = 1

    FALLING_DIVISOR = 2

    INCREASING_FACTOR = 3

    INCREASING_CONSTANT = 1

    height = int(input("Please enter the starting height of the hailstone: "))

    while height > END_HEIGHT:
        
        print("The hailstone is currently at height", height)
        
        if (height % 2) == 0:
            
            height = height // FALLING_DIVISOR

        else:
            
            height = (height * INCREASING_FACTOR) + 1

    print("The hailstone stopped at height", height)



main()
