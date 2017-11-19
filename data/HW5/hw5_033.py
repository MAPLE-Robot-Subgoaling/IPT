def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the bow fill: ")
    fill = input("Please enter a symbol for the box fill: ")
    line1 = outline + (fill * (width - 2)) + outline
    midLines = (line1) * (height - 2)
    middleHeight = [outline] * (height - 2) 
    print(outline * width)
    if width == 1:
        for w in middleHeight:
            print(w)
    else:
        for w in midLines:
            print(w)
    if height > 1:
        print(outline * width)
main()
