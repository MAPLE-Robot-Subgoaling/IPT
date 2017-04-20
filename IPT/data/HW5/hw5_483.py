
def main():

    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outlineSym = input("Please enter a symbol for the box outline: ")
    fillSym = input("Please enter a symbol for the box fill: ")
    
    for h in range(0, height):

         for w in range(0, width):

            if (h == 0 or w == 0 or h == (height-1) or w == (width-1)):
                print (outlineSym, end="")
            else:
                print (fillSym, end="")
         print ("")
main()
            
