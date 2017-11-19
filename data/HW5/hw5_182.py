def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    print (outline * width)
    for i in range (0,height-2):
        o = outline
        f = fill
        print (o + f* (width -2) + o)    
    if height > 1:
        print(outline * width)
main()
