def main():
    height = int(input("Please enter the intial height of the hailstone: "))
    while height > 1:
        print("Hail is currently at height ", height)
        if height % 2 == 0:
            height //= 2
        elif height % 2 == 1:
            height = height * 3 + 1
    print("Hail stopped at height ", height)
main()
