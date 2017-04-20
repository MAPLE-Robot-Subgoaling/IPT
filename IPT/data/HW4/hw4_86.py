
def main():
    endHeight = 1
    height = int(input("Please enter the starting height of the hailstone: "))
    
    print("Hail is currently at height:",height)
    while height != endHeight:
        if (height % 2) == 0:
            height = height // 2
            if height == endHeight:
                print("Hail stopped at height:",height)
            elif height != endHeight:
                print("Hail is currently at height:",height)
        elif (height % 2) != 0:
            height = (height * 3) + 1
            if height == endHeight:
                print("Hail is currently at height:",height)
            elif height != endHeight:
                print("Hail is currently at height:",height)
main()
