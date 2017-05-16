

def main():


    height = int(input("Please enter the starting height of the hailstone: "))
    initHeight = height
    while (height != 1):
        if (height == initHeight):
            print("Hail is currently at height",height)
        if ((height % 2) == 0):
            height = int(height / 2)
            if (height != 1):
                print("Hail is currently at height",height)
            else:
                print("Hail stopped at height 1") 
        else:
            height = (height * 3) + 1
            if (height != 1):
                print("Hail is currently at height",height)
            else:
                print("Hail stopped at height 1")
   
main()
