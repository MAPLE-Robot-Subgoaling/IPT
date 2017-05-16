
def main():
    
    hailHeight = int(input("Please enter the starting height of the hailstone: "))


    if hailHeight == 1:
        print("Hail is stopped at height 1.")
    else:
        print("Hail is currently at height ", hailHeight)

    while hailHeight > 1:
        while (hailHeight % 2) == 0:
            hailHeight = hailHeight / 2
            print("Hail is currently at height ", hailHeight)
        while hailHeight > 1 and (hailHeight % 2) == 1:
            hailHeight = (hailHeight * 3) + 1
            print("Hail is currently at height ", hailHeight)
        if hailHeight == 1:
            print("Hail is stopped at height 1")

main()
