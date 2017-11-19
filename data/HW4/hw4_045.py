def main():
    x = int(input("Please enter the starting height of the hailstone: "))
    while x != 1:
        t = x % 2
        if t == 0:
            x =  x // 2
            sx = str(x)
            print("Hail is currently at height " + sx)
        else:
            x = (x * 3) + 1
            sx = str(x)
            print("Hail is currently at height " + sx)
    sx = str(x)
    print("Hail stopped at height " + sx)
main()
