def boxmaker():
    boxWidth = int(input("Please enter the width of the box."))
    fillWidth = boxWidth - 2
    boxHeight = int(input("Please enter the height of the box."))
    fillHeight = boxHeight - 2
    boxOutline = str(input("Please enter a symbol for the box outline"))
    boxFill = str(input("Please enter a symbol for the box fill."))
    topbotList = [boxOutline]*boxWidth
    middleList = [boxFill]*fillWidth
    print(*topbotList)
    for i in range(fillHeight):
        print(*middleList)
    print(*topbotList)
boxmaker()
