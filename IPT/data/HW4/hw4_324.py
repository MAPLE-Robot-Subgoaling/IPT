


def main():

    height = abs(int(input("Enter the initial height of the hailstone: ")))

    while(height > 1):
        if(height % 2 == 1):
            height = 3 * height + 1
        else:
            height /= 2
        print("The hailstone's current height is: " , int(height))
    
    print("The hailstone stopped at a height of: ", int(height))

    print("\n")
    
main()
