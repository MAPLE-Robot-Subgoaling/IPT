def main():
    height = int(input("Please enter the starting height of a hailstone: "))
    if(height == 1):
        print("Hail stopped and height 1")
    while( height > 2):
        if((height % 2) == 0):
            height = int(height/2)
            print("Hail is currently at height", height)
        if((height % 2) == 1 and height != 1.0):
            height = int((height*3)+1)
            print("Hail is currently at height", height)
    print("Hail stopped and height 1")
main()
