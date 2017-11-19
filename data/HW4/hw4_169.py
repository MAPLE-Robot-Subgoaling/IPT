def main():
    hailstone = int(input("Please enter the starting height of the hailstone: "))
    while( hailstone != 1):
        if hailstone %2 == 0:
            print("Hail is currently at height", hailstone)
            hailstone = int(hailstone/2)
        else:
            print("Hail is currently at height", hailstone)
            hailstone = int((hailstone*3) +1)
    print("Hail stopped at height 1.")
main()
