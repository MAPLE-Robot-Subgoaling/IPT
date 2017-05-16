
def main():

    height = 0

    while (height <= 0):
        height = int(input("Please enter a positive integer for the starting height of the hailstone: "))

    print("Hailstone height is currently " + str(height))
    
    while (height != 1):
        if (height % 2 == 0):
            height = height // 2
            print("Hailstone height is currently " + str(height))
        else:
            height = height * 3 + 1
            print("Hailstone height is currently " + str(height))
    print("Hailstone stopped at height " + str(height))

main()
