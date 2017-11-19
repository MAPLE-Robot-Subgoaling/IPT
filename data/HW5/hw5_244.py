def main():
    width= int(input("Please enter the width of the box:"))
    height= int(input("Please enter the height of the box:"))
    outline= input("Please enter a symbol for the box outline:")
    fill= input("Please enter a symbol for the box fill:")
    fillw= width-2
    fillh=height-2
    print( outline*width)
    fillList=[outline + (fill*fillw)+outline]
    for fillList in range(0,height):
        print(fillList*height)
    print(outline*width)
main()
