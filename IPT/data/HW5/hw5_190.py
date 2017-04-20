


def main ():


    height = int (input ("Please enter the height of the box: "))#height of the boc
    width  = int (input ("Please enter the width of the box: "))#width of the box
    symOut = input ("Please enter a symbol for the outline: ")#outline of the box
    symFill = input ("Please enter a box fill: ")#inside of the box
    controlOuter = (width -1) #fills the top of the box
    controlFill = 0

    for w in range (0,(height-1)): 
 
        print ((symOut * controlOuter) + (symFill * controlFill) + symOut)

        controlOuter = 1 #this is for the outer loop

        controlFill = (width -2) #this increase the inside of the box

    print (symOut * width) #this fills the bottom of the box




main ()
