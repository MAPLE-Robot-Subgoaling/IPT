def main():
    height = int(input("Please enter the starting height of the hailstone: "))
    while height > 1:
        print("Hail is currently at height " + str(int(height)))
        if height / 2 == int(height / 2):
            height = height / 2
        else:
            height = height * 3 + 1
    print("The hail stopped at height " + str(int(height)))
main()
