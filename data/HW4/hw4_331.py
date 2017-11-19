def main():
    height = int(input("Please enter the initial height of the hailstone: "))
    while height > 1:
        print("The hailstone is currently at height", height)
        if height % 2 == 0:
            height = height // 2
        else:
            height = height * 3 + 1
    print("The hailstone stopped at height", height)
main()
