def main():
    height = int(input("Please enter the starting height of the hailstone: "))
    print("Hail is currently at height", height)
    while height > 1:
        if height % 2:
            height = (3 * height +1)
            print("Hail is currently at height", height)
        else:
            height = (height//2)
            if height == 1:
                print("Hail stopped at height", height)
            else:
                print("Hail is currently at height", height)
main()
