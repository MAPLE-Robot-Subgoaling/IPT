def main():
    endHeight = "1"
    endHeight1 = int(endHeight)
    height = int(input("Please enter the starting height of the hailstone: "))
    while height != endHeight1:
        even = 0
        odd = 1
        num = height % 2
        num1 = int(num)
        if num1  == even:
            height = int(height / 2)
            print("Hail is currently at height", height)
        else:
            height = int((height * 3) + 1)
            print("Hail is currently at height", height)
    print("Hail stopped at height", endHeight1)
main()
