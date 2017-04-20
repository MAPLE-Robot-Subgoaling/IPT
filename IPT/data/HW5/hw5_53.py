


def main():


    widthBox = int(input('Please enter the width of the box: '))
    heightBox = int(input('Please enter the height of the box: '))
    symOutline = input('Please enter a symbol for the box outline: ')
    symFill = input('Please enter a symbol for the box fill: ')


    for i in range(heightBox):
        
        if i==0 or i== heightBox-1:
            print(widthBox*symOutline)
            
        
        else:
            print(symOutline+((widthBox-2)*symFill)+symOutline)

            

main()
