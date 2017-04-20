
def main():
    initialHeight = int(input("Please enter the height of the hailstone: "))
    print('Hail is currently at height', initialHeight)
    while initialHeight > 1:
        if initialHeight % 2 == 0:
            initialHeight = (initialHeight // 2)
            if initialHeight > 1:
                print("Hail is currently at height", initialHeight)
        else:
            initialHeight = (initialHeight * 3 + 1)
            if initialHeight > 1:
                print("Hail is currently at height", initialHeight)

    print("Hail stopped at height", initialHeight)

    







main()
