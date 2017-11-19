def main():
    print("\nThis program simulates the movement of a hailstone during a"
       + " storm.\n")
    print("Enter a positive integer to represent the starting  height of the"
       + " hailstone: ")
    height = int(input("<< "))
    if height < 1:
        print("You must enter a height greater than zero, please try again.")
    else:
        while height != 1:
            if height % 2 == 0:
                height = height / 2
            else:
                height = height * 3 + 1
            print("Hail is currently at height", int(height))
        print("Hail stopped at height", int(height))
main()
