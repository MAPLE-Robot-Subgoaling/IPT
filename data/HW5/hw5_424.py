def main():
    widBox = int(input("Please enter ther width of the box:"))
    heightBox = int(input("Please enter the height of the box:"))
    lineBox = input("Please enter a symbol for the box outline:")
    fillBox = input("Please enter a symbol for the box fill:")
    if widBox !=0 and heightBox !=0:
        print(widBox*lineBox)
        for i in range(heightBox-2):
            print(lineBox+(fillBox*(widBox-2))+lineBox)
        if heightBox != 1:
            print(widBox*lineBox)
    else:
        print()
main()
