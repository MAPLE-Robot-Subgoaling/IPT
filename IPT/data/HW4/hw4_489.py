
def main():
    height = int(input("Please enter the starting height of the hailstone: "))
    while(height != 1):
        print("the hail is currently at height", height)
        if((height % 2) == 0):
            height = int(height/2)
        else:
            height = 3*height + 1
    print("the hail stopped at height 1")

main()
