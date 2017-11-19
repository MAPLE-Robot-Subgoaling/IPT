def main():
    odd = 1  
    even = 0 
    height = int(input("Please enter the starting height of the hailstone: "))
    print("Hail is currently at height",height)
    while height != 1:
        if (height % 2) == even: 
            height = height * 0.5
            height = int(height)
            print("Hail is currently at height",height)
        elif (height % 2) == odd: 
            height = 3 * height + 1
            height = int(height)
            print("Hail is currently at height",height)
    print("Hail stopped at height",height)
main()
