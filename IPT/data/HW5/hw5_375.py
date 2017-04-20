
def main():

    userWidth = int(input("Please enter the width of the box: "))

    userHeight = int(input("Please enter the height of the box: "))

    userSymbolOutline = input("Please enter a symbol for the box outline: ")

    userSymbolFill = input("Please enter a symbol for the box fill: ")
    
    for n in range(0, userHeight):

        widthOverall = userWidth * userSymbolOutline
 
        lastVariable = userHeight - 1

        middleSymbols = userWidth - 2

        symbolFillOverall = middleSymbols * userSymbolFill 

        if n == 0 or n == lastVariable:

           print(widthOverall)

        else :
      
           print(userSymbolOutline + symbolFillOverall + userSymbolOutline)



main()
