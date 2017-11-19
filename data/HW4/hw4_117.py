def main():
    height = int(input("Please enter the starting height of the hailstone: "))
    while(height > 1):
        if(height % 2 == 0 and height != 1):
            print("Hail is currently at height " + str("%d" % height))
            height = height/2
        if(height % 2 != 0 and height != 1):
            print("Hail is currently at height " + str("%d" % height))
            height = (height * 3) + 1
    print("Hail is stopped at height " + str("%d" % height))
main()
