
def main():

    height = int(input("Please enter the starting height: "))
    
    while height != 1:


        if height % 2 == 1:
            print("Hail is currently at height", int(height))
            height =(3* height) + 1


        elif height % 2 == 0:
            print("Hail is currently at height", int(height))
            height = height/2

    print("Hail stopped at height 1")

main()
