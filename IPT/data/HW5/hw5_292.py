def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbolout = input("Please enter a symbol for the box outline: ")
    symbolfill = input("Please enter a symbol for the box fill: ")
    list1 = list(range(height-2))
    print(symbolout*width)
    for i in list1: 
        print(symbolout+symbolfill*(width-2)+symbolout)
        i+1
    if(height!=1):
        print(symbolout*width)
main()
