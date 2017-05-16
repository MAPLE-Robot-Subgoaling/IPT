def partTwo():
    BOX_WIDTH = int(input("Please enter a box width: \n"))
    BOX_HEIGHT = int(input("Please enter a box height: \n"))
    BOX_OUTLINE_SYMBOL = (input("Please enter a box outline symbol: \n"))
    BOX_FILL_SYMBOL = (input("Please enter a box fill symbol: \n"))
    BOX_STRING = ""
    for runningRow in range(BOX_HEIGHT):
       if(runningRow == 0 or runningRow == BOX_HEIGHT - 1):
           BOX_STRING += BOX_OUTLINE_SYMBOL * BOX_WIDTH
       else:
           BOX_STRING += BOX_OUTLINE_SYMBOL + BOX_FILL_SYMBOL * (BOX_WIDTH - 2) + BOX_OUTLINE_SYMBOL
           
       BOX_STRING += "\n"
    print(BOX_STRING)
partTwo()
