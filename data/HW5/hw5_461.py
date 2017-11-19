def main():
    width = int(input("Enter box width: "))
    height = int(input("Enter box height: "))
    outChar = input("Enter box outline character: ")
    fillChar = input("Enter box fill character: ")
    for n in range(height):
        boxLine = ""
        if n == 0 or n == height - 1:
            boxLine = outChar * width
        else:
            boxLine = outChar + fillChar * (width - 2) + outChar
        print(boxLine)
main()
