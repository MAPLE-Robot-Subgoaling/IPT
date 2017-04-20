def main():
    height = int(input("What is the starting height of the hailstone? "))
    while (height != 1):
        if (height % 2 == 0):
            height /= 2
        elif (height % 2 == 1):
            height = height * 3 + 1
        print("The current height of the hailstone is:", height)
    
    print("The hailstone finally hit the ground at height",height,"!")




main()
