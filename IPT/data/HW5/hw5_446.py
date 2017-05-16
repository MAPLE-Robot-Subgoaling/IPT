

def main():


    widthBox = int(input("Please enter the width of the box: "))
    heightBox = int(input("Please enter the height of the box: "))
    symbolBoxOut = input("Please enter a symbol for the box outline: ")
    symbolBoxFill = input("Please enter a symbol for the box fill: ")

    print(symbolBoxOut * widthBox)
    
    for i in range(heightBox-2):
        print(symbolBoxOut + symbolBoxFill * (widthBox - 2)+ symbolBoxOut)
   
    if heightBox > 1:

        print(symbolBoxOut * widthBox)
                       

main()




