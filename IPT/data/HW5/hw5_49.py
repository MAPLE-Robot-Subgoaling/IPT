
def main(): 

    height = int(input("Please enter the height of the box: "))
    width = int(input("Please enter the width of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    
    widthLine = outline + (fill * (width - 2)) + outline
    centerPieces = [widthLine] * (height - 2)  
    middleHeight = [outline] * (height-2) #This is the height of the box, taking into account the top and bottom print statements.

    print(outline * width)
    if width == 1: 
        for w in middleHeight:
            print(w)
    else: 
        for w in centerPieces: 
            print(w)
    if height > 1:
        print(outline * width) 
    
main()

