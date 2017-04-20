
def main():
    c = 0
    hailstone_height = int(input("Please enter the starting height of the hailstone: "))
    while c == 0:
        if hailstone_height != 1:
            print("Hail is currently at height", int(hailstone_height))
        if int(hailstone_height)  == 1:
            print("Hail stopped at height 1")
            c = 1
        elif hailstone_height % 2  == 0:
            hailstone_height = hailstone_height / 2
        elif hailstone_height % 2 != 0:
            hailstone_height = (hailstone_height * 3) + 1
main()
