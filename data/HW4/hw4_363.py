def main():
    num = print(int(input("Enter the starting height of the hailstone.")))
    if num != 1:
        print("Hail is currently at ,num")
    elif num is "even":
        num = num % 2
        print("Hail is currently at ,num")
    elif num is "odd":
        num = num x 3 + 1
        print("Hail is currently at ,num")
    else:
        print("Hail stopped at height 1.")
main()
