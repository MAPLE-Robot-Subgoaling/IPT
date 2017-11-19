def main():
    height = int(input("Input hailstone starting height: "))
    while height != 1:
        print("Hail Height:", height)
        if height % 2 == 0:
            height = height // 2
        else:
            height = height * 3 + 1
    print("Hail stopped at height:", height)
main()
