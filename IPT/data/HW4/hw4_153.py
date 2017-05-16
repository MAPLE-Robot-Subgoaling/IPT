
def main():
    height = int(input("Please enter the starting height of the hailstone: "))
    if height == 1:
        print("Hail stopped at height 1")
    else:
        while height > 1:
            print("Hail is currently at the height", height)
            evenCheck = height % 2
            if evenCheck == 0:
                height = int(height / 2)
            else:
                height = int((height * 3) + 1)
            if height == 1:
                print("Hail stopped at height 1")
main()
