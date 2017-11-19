def main():
    height = int(input("Please enter the starting height of the hailstone: "))
    print ("Hail is currently at height",height)
    while height > 1:
        if height % 2 == 0:
            height = int(height/2)
        else:
            height = int((height*3)+1)
        if height > 1:
            print ("Hail is currently at height",height)
        else:
            print("Hail stopped at height",height)
main()
