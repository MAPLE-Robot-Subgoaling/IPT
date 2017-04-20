
def main():

    width = int(input("Please enter the width of the box:"))
    hieght = int(input("Please enter the height of the box:"))
    symbol = input("Please enter a symbol for the box outline;")
    boxFill = input("Please enter a symbol for the box fill;")
    count = 0
    
    if hieght== 1:
        print(width * symbol)

    else :
        print(width * symbol)
        while (hieght - 2 > count):
            print(symbol+boxFill * (width-2)+symbol)
            count = count +1 
            
        print(width * symbol)
    
    







main()
