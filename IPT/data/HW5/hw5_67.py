def main():
    width= int(input("please enter the width of the box: "))
    length= int(input("please enter the length of the box : "))
    symbol1= input("please enter the symbol for the box outline: ")
    symbol2= input("please enter the symbol for the box fill: ")

    for box in range(length):
        if box == 0 or box == (length-1):
                    print(symbol1*width)
        else:
                    print(symbol1+(symbol2*(width-2))+ symbol1)




main()
