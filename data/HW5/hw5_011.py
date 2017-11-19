def main():
    height = (int)(input("What is the height of the box? "))
    width = (int)(input("What is the width of the box? "))
    outline = input("What is the outline symbol of the box? ")
    filled = input("What is the filled in symbol of the box? ")
    for y in range(0, height, 1):
        currentLine = "" 
        if y == 0 or y == (height-1): 
            currentLine = outline*width
        else: 
            currentLine = currentLine + outline 
            currentLine = currentLine + filled*(width-2) 
            currentLine = currentLine+outline 
        print(currentLine) 
main()
