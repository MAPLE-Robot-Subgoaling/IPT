def main(): 
    box = []
    columns =int( input("Please enter the width of the box: "))
    rows =int(input("Please enter the height of the box: "))
    outline = str(input("What symbol will the box be outlined in? "))
    fill = str(input("What symbol will the box be filled with? "))
    newRows = rows - 1 
    newColumns = columns - 1 
    for n in range(rows):
        innerList = []
        printList = ""
        box.append(innerList)
        for m in range(columns):
            if ((n == 0) or (n == newRows) or (m == 0) or (m == newColumns)):
                innerList.append(outline) 
                if (printList != ""):
                    printList = printList + " " + outline
                else:
                    printList = printList + outline
            else:
                innerList.append(fill) 
                printList = printList + " " + fill
        print(printList)
main() 
