
def main():

    height = int(input("What is the starting height of the hailstone? "))

    while height != 1:
        
        if (height % 2) != 0:

            height = (height * 3) + 1
            
            print("Hail is currently at height ",height)

        if (height % 2) == 0:

            height = (height // 2)

            print("Hail is currently at height ",height)

    print("Hail stopped at height 1")


main()
    
        
