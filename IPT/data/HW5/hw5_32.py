
def main():


    boxWidth = int(input( "Please enter the width of the box:  "))
    boxHeight = int(input( "Please enter the height of the box:  "))
    boxOutline = input( "Please enter a symbol for the box outline:  ")
    boxFill = input( "Please enter a symbol for the box fill:  ")
    OUTLINE = 2


    print (boxOutline*boxWidth)


    for i in range(0,boxHeight-OUTLINE):
        print (boxOutline+(boxFill*(boxWidth-OUTLINE))+boxOutline)
    
    if boxHeight > 1:
        print (boxOutline*boxWidth)










main()
