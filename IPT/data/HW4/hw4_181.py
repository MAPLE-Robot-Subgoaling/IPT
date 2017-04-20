
def main():
    height = int(input("Please enter the starting height of the hailstone: "))
    while height != 1:
        odd_or_even = height % 2
        if odd_or_even == 0:
            height = height // 2
            print("Hail is currently at height", height)
        else:
            height = (height * 3) + 1
            print("Hail is currently at height", height)
    print("Hail stopped at height 1")

main()

