def main():
    HEIGHT_ONE = 1
    EVEN_CHECK = 2
    initialHeight = int(input("Please enter the starting height of the hailstone: "))
    evenOdd = initialHeight % EVEN_CHECK
    while initialHeight != 1:
        if evenOdd == 1:
            initialHeight = int(initialHeight * 3 + 1)
            evenOdd = initialHeight % EVEN_CHECK
            print("Hail is curruntly at height ", initialHeight)
        if evenOdd == 0:
            initialHeight = int(initialHeight / 2)
            evenOdd = initialHeight % EVEN_CHECK
            print("Hail is currently at height ", initialHeight)
    if initialHeight == 1:
        print("Hail stopped at height 1")
main()
