def main():
    height = int(input("Please enter the starting height of the hailstone: "))
    while(height > 1):
        height = str(height)
        print("Hail is currently at height",height)
        height = int(height)
        if height % 2 == 0:
            height = height//2
        else:
            height = height*3+1
    height = str(height)
    print("Hail stopped at height",height)
main()
