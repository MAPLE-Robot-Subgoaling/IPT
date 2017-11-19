def main (): 
    hailstone = int(input("What is the starting height of the hailstone: "))
    print("The hailstone is currently at height: ", hailstone) 
    while  hailstone != 1: 
        if hailstone % 2 == 1: 
            hailstone = (hailstone * 3) + 1
            print("The hailstone is currently at height: ", hailstone)
        else: 
            hailstone = (hailstone // 2) 
            print("The hailstone is currently at height: ", hailstone)
    print("Hail stopped at 1 height 1.")
main()
