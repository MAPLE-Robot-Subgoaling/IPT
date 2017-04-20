
def main():

    height = int(input("Pleas enter the starting height of the hailstone: "))

    while height != 1:

        if height % 2 == 0:
            print("Hail is currently at height", height)
            height = height // 2
    
        elif height % 2 != 0:
            print("Hail is currently at height", height)
            height = height * 3 + 1

    if height == 1:
        print("Hail stopped at height 1.")

main()
    
