
def main():
    height = int(input("Enter a height for the hailstorm: "))
    evenOdd = height % 2
    while height != 1:
        while evenOdd == 0:
            height = int(height / 2)
            evenOdd = height % 2
            print("Hail is currently at height",height)
        while evenOdd == 1 and height != 1:
            height = int((height * 3) + 1)
            evenOdd = height % 2
            print("Hail is currently at height",height)
    print("Hail stopped at height 1")
    
main()
