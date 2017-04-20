
def main():
    height = (int)(input("What is the height of the box? "))
    width = (int)(input("What is the width of the box? "))
    outline = input("What is the outline symbol of the box? ")
    filled = input("What is the filled in symbol of the box? ")

    for y in range(0, height, 1):
        currentLine = "" #reset
        if y == 0 or y == (height-1): #top and bottom of box
            currentLine = outline*width
        else: #middle of box
            currentLine = currentLine + outline #nearside of box outline
            currentLine = currentLine + filled*(width-2) #fill middle of box
            currentLine = currentLine+outline #farside of box outline
        print(currentLine) #print box line by line

main()
