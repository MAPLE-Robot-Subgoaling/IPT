
def main():

    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline_symbol = input("Please enter a symbol for the box outline: ")
    fill_symbol = input("Please enter a symbol for the box fill: ")

    widthList = list(range(0, width + 1))
    heightList = list(range(0, height))

 
      
    for n in heightList:
        if n == 0 or n == height-1:
             print(outline_symbol*width)
        else:
             print(outline_symbol + (fill_symbol*(width-2)) + outline_symbol)
 


main()
