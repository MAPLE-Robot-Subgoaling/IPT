def main():
    stHeight = int(input("Please enter the starting height of the hailstone: "))
    while stHeight % 2 == 0:
        print("Hail is currently at height", stHeight / 2)
        ansHeight = stHeight / 2
        if ansHeight % 2 == 0:
            print("Hail is currently at height", ansHeight / 2)
        else stHeight != 0: 
            print("Hail is currently at height", (stHeight * 3) + 1)
main()
