def main():
    valid = 0
    while valid == 0:
        height = int(input("Please enter the starting height of the hailstone: "))
        if height < 1:
            print("Please enter an integer greater than or equal to 1 next time.")
        else:
            valid = 1
    while height != 1:
        print("Hail is currently at height ",height)
        if height % 2 == 0:
            height = height / 2
        else:
            height = height * 3 + 1
    print("Hail stopped at height ",height)
main()
