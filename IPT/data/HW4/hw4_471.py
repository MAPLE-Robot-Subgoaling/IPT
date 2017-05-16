
def main():

    height = int(input("Please enter the starting height of the hailstorm: "))
    
    while ( height % 2 != 0 ):
        if (height == 1):
            break

        print("Hail is currently at height ", height)
        height = (height * 3) + 1

        while ( height % 2 == 0 ):
            print("Hail is currently at height ", height)
            height = height // 2
            
            if (height == 1):
                print("Hail stopped at height 1")
    
    while ( height % 2 == 0 ):
        print("Hail is currently at height ", height)
        height = height // 2
        
        if (height == 1):
            print("Hail stopped at height 1")
            break

        while ( height % 2 != 0 ):
            print("Hail is currently at height ", height)
            height = (height * 3) + 1

main()

    
