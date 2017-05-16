def main():
    num1 = int(input("Please enter the width of the box: ")) 
    num2 = int(input("Please enter the height of the box: "))
    symbol1 = input("Please enter a symbol for the box outline: ")
    symbol2 = input("Please enter a symbol for the box fill: ")
    boxTop = ""
    insideBox = ""
    for i in range(num1): # This loop constructs the top and bottom of the box
        boxTop = boxTop + symbol1 
    for n in range(num2 + 1): # This loop ensures the box does not exceed 
        if n == 1 or n == num2: # This if statement prints out the top and 
            print(boxTop)
        elif n < num2 and n > 1: # This if statement defines how and when the 
            insideBox = "" # Resets the inside of the box so that the length is
            for j in range(num1 + 1): # This loop creates the inside of the box
                if j == 1 or j == num1: # This if statement sets when the 
                    insideBox = insideBox + symbol1
                elif j < num1 and j > 1: # This if statement sets when the 
                    insideBox = insideBox + symbol2
            print(insideBox) # prints the inside of the box for the user    
main()
