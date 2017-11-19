def main():
    height = int(input("Please enter the height of the hailstone: "))
    while height != 0 and height != 1:
        if height % 2 == 0:
            height = height / 2
            print ("Hailstone is currently at height", height)
        elif height % 2 != 0:
            height = (height * 3) + 1
            print ("Hailstone is currently at height", height)
main()
