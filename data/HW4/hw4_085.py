def main():
    height = int(input("What is the starting height of the hailstone? "))
    while height > 1:
        print("The hailstone is at height", height)
        if height % 2 == 0:
            height = height // 2
        else:
            height = height * 3 + 1
    print("The hailstone is at height", height)
main()
