def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = str(input("Please enter a symbol for the box outline: "))
    fill = str(input("Please enter a symbol for the box fill: "))
    cube =""
    outside = outline*width
    inner = fill*width
    if len(inner)>2:
        inner = inner[:0] + outline + inner[1:]
        inner = inner[:width-1] + outline 
    for i in range(0, width):
        cube=outside
    if height>1:
        if height==2:
            for i in range(0, 1):
                cube=cube+"\n"+cube
        elif height>2:
            for i in range(0, height):
                cube=cube
                if i ==0:
                    print (cube)
                elif i!=0 and i!=height-1:
                    print(inner)
                elif i == height-1:
                    print(cube)
    else:
        print(cube)
main()
