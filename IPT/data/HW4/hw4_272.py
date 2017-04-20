
def main():
    start = int(input("Please enter the starting height of the hailstone: "))
    print("Hail is currently at height", int(start))
    while start != 2:
        if start % 2 == 0:
            start = start / 2
            print("Hail is currently at height", int(start))
        elif start % 2 == 1:
            start = start * 3 + 1
            print("Hail is currently at height", int(start))
    print("Hail stopped at height 1")


main()
