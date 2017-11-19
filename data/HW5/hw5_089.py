def main():
    num1 = int(input("Please enter the width of the box: ")) 
    num2 = int(input("Please enter the height of the box: "))
    symbol1 = input("Please enter a symbol for the box outline: ")
    symbol2 = input("Please enter a symbol for the box fill: ")
    boxTop = ""
    insideBox = ""
    for i in range(num1): 
        boxTop = boxTop + symbol1 
    for n in range(num2 + 1): 
        if n == 1 or n == num2: 
            print(boxTop)
        elif n < num2 and n > 1: 
            insideBox = "" 
            for j in range(num1 + 1): 
                if j == 1 or j == num1: 
                    insideBox = insideBox + symbol1
                elif j < num1 and j > 1: 
                    insideBox = insideBox + symbol2
            print(insideBox) 
main()
