def main():
    height = int(input("Please enter the height of the hailstone: "))
    print("Hail is currently at height " , height)
    while height != 1:
        while (height % 2 == 0) and (height != 1):
            height = height / 2
            print("Hail is currently at height " , height)
        while (height % 2 == 1) and (height != 1):
            height = (3 * height + 1)
            print("Hail is currently at height " , height)
    print("Hail stopped at height 1")
main ()
