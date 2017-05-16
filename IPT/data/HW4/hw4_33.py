
def main():
    numHeight = int(input("Please enter the starting height of the hailstone: "))
    print("Hail is currently at height", numHeight)
    while numHeight != 1:
        if numHeight % 2 == 0:
            numHeight = numHeight // 2
            print("Hail is currently at height", numHeight)
        elif numHeight % 2 == 1:
            numHeight = numHeight * 3 + 1
            print("Hail is currently at height", numHeight)
    print("Hail stopped at height", numHeight)

main()
