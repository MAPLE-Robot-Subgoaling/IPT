def main():
    height=int(input("Please enter the starting height of the hailstone: "))
    height>0
    while height > 0 and height != 1:
        if height % 2 == 0:
            print ("Hail is currently at height ", height)
            height = height/2
        if height % 2 == 1 and height !=1:
            print ("Hail is currently at height ", height)
            height = (height*3)+1
        if height == 1:
            break
    while height == 1:
        print ("Hail has stopped at height 1")
        break
main()
