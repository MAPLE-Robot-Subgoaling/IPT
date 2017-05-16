def main():
    boxWidth = int(input("Input box width: "))
    smallaWidth = boxWidth-2
    if smallaWidth < 1:
        smallaWidth = 0
    boxHeight = int(input("Input box height: "))
    smallaHeight = boxHeight - 2
    boxOutline = input("Input box outline: ")
    boxFill = input("Input box filler: ")
    print(boxOutline*boxWidth)
    if boxHeight >= 3:
        for mm in range(smallaHeight):
           if boxWidth >= 3:
               print(boxOutline+boxFill*smallaWidth+boxOutline)
           else:
               print(boxOutline*boxWidth)
    if boxHeight >= 2:
       print(boxOutline*boxWidth)
main()
