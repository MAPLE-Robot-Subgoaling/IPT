
def main():

    print("Please enter the width of the box:")
    width = int(input())
    print("Please enter the height of the box:")
    height = int(input())
    print("Please enter a symbol for the box outline:")
    symbolOut = input()
    print("Please enter a symbol for the box fill:")
    symbolIn = input()

    for interval in range(height):
        currentLine =""
        if interval == 0 or interval == height - 1:
            for interval in range(width):
                currentLine = currentLine + symbolOut
        else:
            for interval in range(width):
                if interval == 0 or interval == width-1:
                    currentLine = currentLine + symbolOut
                else:
                    currentLine = currentLine + symbolIn
        print(currentLine)
        

main()
