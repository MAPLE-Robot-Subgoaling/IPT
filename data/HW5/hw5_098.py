def main ():
    height = int (input ("Please enter the height of the box: "))
    width  = int (input ("Please enter the width of the box: "))
    symOut = input ("Please enter a symbol for the outline: ")
    symFill = input ("Please enter a box fill: ")
    controlOuter = (width -1) 
    controlFill = 0
    for w in range (0,(height-1)): 
        print ((symOut * controlOuter) + (symFill * controlFill) + symOut)
        controlOuter = 1 
        controlFill = (width -2) 
    print (symOut * width) 
main ()
