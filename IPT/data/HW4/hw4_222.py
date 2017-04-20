def main():
    height=int(input("Enter the height of the hailstone: "))
    while height > 1:
        print("The current height is",height)
        if(height % 2) == 0:
            height = int(height / 2)
        else:
            height = int((height*3)+1)
    print("It is height",height,", Hail stopped")
main()
