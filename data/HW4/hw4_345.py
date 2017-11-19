def main(): 
    heightHailstone = int(input("Please enter the starting height of the hailstone: "))
    while(heightHailstone != 1):
        print("Hail is currently at height", heightHailstone)
        if ((heightHailstone % 2) == 0):
            heightHailstone = heightHailstone//2
        elif ((heightHailstone % 2) != 0):
            heightHailstone = (heightHailstone*3)+1
        if (heightHailstone == 1):
            print("Hail stopped at height", heightHailstone)
main()
