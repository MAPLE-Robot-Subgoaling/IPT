
def main():
    boxWidth = int(input("Please enter the width of the box: "))
    boxHeight = int(input("Please enter the height of the box: "))
    boxOutline = input("Please enter a symbol for the box outline: ")
    boxFiller = input("Please enter a symbol for the box fill: ")
    
    for i in range(boxHeight):
        if i == 0 or i == (boxHeight - 1):
            print(boxOutline * boxWidth)
        else:
            print(boxOutline + (boxFiller*(boxWidth - 2)) + boxOutline)  
        
main()
