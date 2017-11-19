def main():
    height = int(input("Please enter the height of your box "))
    width = int(input("Please enter the width of your box "))
    OUTLINE = input("Please enter a symbol to outline your box ")
    FILL = input("Please enter a symbol to fill your box ")
    listWidth = list(range(width))
    listHeight = list(range(0, height - 2)) 
    print(len(listWidth) * OUTLINE)
    for h in listHeight:
        str(OUTLINE)
        fillMiddle = str((len(listWidth) - 2) * FILL)
        print((OUTLINE + fillMiddle +  OUTLINE))
    print(len(listWidth) * OUTLINE)
main()
