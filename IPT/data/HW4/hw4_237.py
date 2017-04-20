
def main():

    height = int(input("Pease enter the starting height of the hailstone: "))
    
    while height != 1:

        print("Hail is currently at height",height)

        if height % 2 == 1:
            height = height*3 + 1

        else:
            height = height//2

    print("Hail stopped at height",height)

main()
