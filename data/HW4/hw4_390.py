def main():
    height = int(input("Please enter the starting height of the hailstone: "))
    while height > 1:
        print("Hail is currently at hight", height)
        if height % 2 != 0:
            height = int(height * 3 + 1)
        else:
            height = int(height / 2)               
    print("Hail stopped at height", height)
main()
