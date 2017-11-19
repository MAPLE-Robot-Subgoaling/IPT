def main():
    height = int(input("Enter the starting height of the hailstone."))
    while (height > 1):
        if (height % 2 == 0):
            height = height / 2
        else:
            height = (height * 3) + 1
        print("Current height is " + str(height))
main()
