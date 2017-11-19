def main():
    height = int(input("Please enter the starting height of the hailstone: "));
    while height != 1:
        print("Hail is currently at height " + str(height));
        if height % 2 == 1:
            height = height * 3 + 1;
        else:
            height //= 2;
    print("Hail stopped at height 1");
main()
