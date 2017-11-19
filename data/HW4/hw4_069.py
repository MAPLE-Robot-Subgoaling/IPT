def main():
    currentHeight = int(input("Please enter the starting height of the hailstone: "))
    while currentHeight > 1:
        print("Hail is currently at height" , currentHeight)
        if currentHeight % 2 == 0:
            currentHeight = currentHeight // 2
        else:
            currentHeight = currentHeight * 3 + 1
    if currentHeight == 1:
        print("Hail stopped at 1")
main()
