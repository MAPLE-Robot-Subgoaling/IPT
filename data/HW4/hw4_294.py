def main():
    height = int(input("Please enter the starting height of the hailstone: "))
    while(height != 1):
        while(height % 2 == 0):
            height = height//2
            if(height != 1):
                print("Hail is currently at height", height)
        while((height % 2 == 1)and(height != 1)):
            height = (height*3)+1
            print("Hail is currently at height", height)
    if(height == 1):
        print("Hail stopped at height 1")
main()
