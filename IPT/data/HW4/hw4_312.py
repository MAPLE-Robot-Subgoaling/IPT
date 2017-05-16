
def main():
    height = input("Please enter the current height of the hailstone: ")
    height = int(height)
    while(height > 1):
        height = int(height)
        print("The hailstone is at height",height)
        if(height % 2 == 0):
            height /= 2
        elif(height % 2 != 0):
            height *= 3
            height += 1
    print("The hailstone stopped at height 1")

main()
