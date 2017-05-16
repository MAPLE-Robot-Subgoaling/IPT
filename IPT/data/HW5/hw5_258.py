

def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the hight of the box: "))
    outline = str(input("Please enter a symbol for the box outline: "))
    fill = str(input("Please enter a symbol for the box fill: "))
    box = [""]*height
    for h in range(height):
        for w in range(width):
            if h == 0 or h == height - 1 or w == 0 or w == width - 1:
                box[h] = box[h] + outline
            else:
                box[h] = box[h] + fill
    for row in box :
        print ( row )
    


main()
