def main():
    height= int(input("Enter the current height of the hailstone:"))
    height > 0
    while height != 1:
        if height % 2 == 0:
            height= height//2
            print("Hail is currently at height", height)
        else:
            height= (height * 3) + 1
            print("Hail is currently at hieght", height)
    print("Hail stopped at height 1")
main()
