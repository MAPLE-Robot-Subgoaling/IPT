def main():
    heightHailstone = int(input("Please enter the starting height of the hailstone: "))
    print("Hail is currently at height", heightHailstone)
    while heightHailstone != 1:
        evenOrOdd = heightHailstone % 2
        if evenOrOdd == 0:
            heightHailstone = heightHailstone // 2
            if heightHailstone != 1:
                print("Hail is currently at height", heightHailstone)
        if evenOrOdd == 1:
            heightHailstone = (heightHailstone * 3) + 1
            if heightHailstone != 1:
                print("Hail is currently at height", heightHailstone)
    print("Hail stopped at height", heightHailstone)
main()
