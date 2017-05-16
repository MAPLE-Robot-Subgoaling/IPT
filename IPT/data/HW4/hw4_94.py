

def main():
    height = int(input("Please enter the starting height of the hailstone: "))
    while height != 1:
        print("Hail is currently at height", height)
        evenness = height % 2
        if evenness == 0:
            height = height // 2
        else:
            height = height * 3
            height = height + 1
    print("Hail stopped at height", height)
main()
