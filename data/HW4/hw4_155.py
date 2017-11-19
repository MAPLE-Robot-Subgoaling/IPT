def main() :
    MIN_HEIGHT = 1
    height = int(input("Please enter the starting height of the hailstone: "))
    while height != 1 :
        print("Hail is currently at height", height)
        if height%2 == 0 :
            height = int(height/2)
        else :
            height = int((height*3)+1)
    print("Hail stopped at height 1")
main()
