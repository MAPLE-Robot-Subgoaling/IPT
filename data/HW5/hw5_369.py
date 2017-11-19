def main():
    boxH = []    
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = str(input("Please enter a symbol for the box outline: "))
    fill = str(input("Please enter a symbol for the box fill: "))
    FILLING = 2
    STOPPER = 1
    print(outline * width)
    while height != FILLING and height >= FILLING:
        boxH.append(height)
        height = (height - STOPPER)
    for test in boxH : 
        print (outline + (fill* (width-FILLING)) + outline)
    if height > STOPPER:
        print(outline * width)
main()
