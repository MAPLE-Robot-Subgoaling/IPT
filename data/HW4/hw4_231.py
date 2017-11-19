def main():
    hailstone = int(input("Please enter the starting height of the hailstone: " ))
    print("Hail is currently at height", hailstone)
    while hailstone != 1:
        if (hailstone % 2) == 0:
            hailstone = (hailstone // 2)
            print("Hail is currently at height", hailstone)
        else:
            hailstone = (hailstone*3)+1 
            print("Hail is currently at height", hailstone)
    print("Hail stopped at height 1")
main()
