
def main () :

    height = int(input("Please enter the starting height of the hailstone: "))
    while height != 1:
        if (height % 2 == 0) and height != 1 :      #even
            print ("Hail is currently at height",height,)
            height = (height//2)
        if (height % 2 != 0) and height != 1 :      #odd
            print ("Hail is currently at height",height,)
            height = ((height*3)+1)

    print ("Hail stopped at height",height,)



main ()
