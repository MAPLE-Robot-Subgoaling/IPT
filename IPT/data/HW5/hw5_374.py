

def main(): 



    boxWidth = int(input('Please enter the width of the box: '))
    boxHight = int(input('Please enter the hight of the box: '))
    outSymbol = input('Please enter a symbol for the box outline: ')
    fillSymbol = input('Please enter a symbol for the box fill: ')

    outBox = boxWidth * outSymbol
    print(outBox)



    for body in range(1, boxHight - 1, 1):
 
        bodyBox = outSymbol + ((boxWidth-1) * fillSymbol) + outSymbol 
        print(bodyBox)


    if boxHight > 1 and boxWidth > 1: 

        print(outBox)
    








main()
