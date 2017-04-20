



def main():

    width = int( input( "Please enter the width of the box: ") )
    height = int( input ( "Please enter the height of the box: ") )
    outSymbol = input( "Please enter a symbol for the box outline: " )
    fillSymbol = input( "Please enter a sumbol for the box fill: ") 

    for box in range(height) :
        
        if box == 0:
            print ( outSymbol * width ) 
        elif box != (height - 1) :
            print ( outSymbol + fillSymbol * (width - 2) + outSymbol )
        else:
            print ( outSymbol * width )

main()
