def main():
    width = int(float(input("Please enter the width of the box: ")))
    height = int(float(input("Please enter the hieght of the box: ")))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    EDGE = 2
    height=height-EDGE
    print(width*outline)
    while height > 0:
        print(outline,(width-EDGE)*fill,outline)
        height-=1
    print(width*outline)
main()
