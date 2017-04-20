
def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    
    border = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")

    for i in range(height):
        currentLine = border
        if ((i == 0) or ((i+1) == height)):
            for j in range(width-2):
                currentLine = currentLine + border
        else:
            for j in range(width-2):
                currentLine = currentLine + fill
        currentLine = currentLine + border
        print(currentLine)

main()
