
def main():
    odd = 1  #will mod the height and if remainder is 1, it is odd
    even = 0 #will mod the height and if remainder is 0, is is even
    
    height = int(input("Please enter the starting height of the hailstone: "))
    print("Hail is currently at height",height)
    while height != 1:
        if (height % 2) == even: #checking if odd height
            height = height * 0.5
            height = int(height)
            print("Hail is currently at height",height)
        elif (height % 2) == odd: #checking if even height
            height = 3 * height + 1
            height = int(height)
            print("Hail is currently at height",height)
    print("Hail stopped at height",height)
main()
