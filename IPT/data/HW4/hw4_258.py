def main():
    height = int(input("Please enter the starting height of the hailstone: "))
    while height != 1:
        print("Hail is currently at height", height)
        if ( height % 2 ) == 0 :
            height = height//2
        else:
            height = height*3
            height +=1
    print("Hail stopped at height 1")





main()
