
def main():

    height = int(input("Enter the starting height of the hailstone: "))

    while height != 1:
        
        print("Hail is currently at height", height)
        
        if height % 2 == 0:
            height = height // 2

        else:
            height = (3 * height) + 1

    print("Hail stopped at height",height)

main()
