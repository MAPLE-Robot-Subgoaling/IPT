def main():
    height=int(input("Please enter the starting height of the hailstone:"))
    while height != 1:
        even = height % 2
        if even == 1:
            height = height * 3 + 1
            print("Hail is currently at height", int(height))
        if even == 0:
            height = height / 2
            print("Hail is currently at height", int (height))
main()
