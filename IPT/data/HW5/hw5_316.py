
def main():
    boxWidth = int(input("Please enter the width of the box: "))
    boxHeight = int(input("Please enter the height of the box: "))
    symOut = input("Please enter a symbol for the box outline: ")
    symFill = input("Please enter a symbol for the box to fill: ")
    
    for i in range(boxHeight):
        if i == 0 or i == boxHeight - 1:
            line = ""
            for j in range(boxWidth):
                line += symOut
            print(line)
        else:
            line = ""
            for j in range(boxWidth):
                if j == 0 or j == boxWidth - 1:
                    line += symOut
                else:
                    line += symFill
            print(line)
main()
