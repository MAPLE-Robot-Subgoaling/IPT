
def main():

    boxWidth=int(input("Please enter the width of the box: "))
    boxHeight=int(input("Please enter the height of the box: "))
    boxOutline=input("Please enter a symbol for the box outline: ")
    boxFill=input("Please enter a symbol for the box fill: ")

    print(boxWidth * boxOutline)
    
    for h in range(1,boxHeight-1):

        if boxWidth != 1:
            print(boxOutline+boxFill*(boxWidth-2)+boxOutline)
        elif boxWidth >= 1:
            print(boxOutline)

    if boxHeight != 1:
        print(boxWidth * boxOutline)

main()
