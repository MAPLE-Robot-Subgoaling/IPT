def main():
    num = int(input("Enter starting height of the hailstone: "))
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = (num * 3) + 1
        print("Hail is currently at height 36", num)
main()
