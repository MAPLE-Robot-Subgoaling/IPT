
def main(): # Start program
    

    box = []# Create outer list
    columns =int( input("Please enter the width of the box: "))# number of columns
    rows =int(input("Please enter the height of the box: "))# number of rows
    outline = str(input("What symbol will the box be outlined in? "))# perimeter/outline character
    fill = str(input("What symbol will the box be filled with? "))# center/fill character
   
    newRows = rows - 1 # Set number of rows
    newColumns = columns - 1 # set number of columns
    
    for n in range(rows):
        innerList = []
        printList = ""
        box.append(innerList)# Insert inner list in to outer list
        for m in range(columns):
            if ((n == 0) or (n == newRows) or (m == 0) or (m == newColumns)):# use oultline character
                innerList.append(outline) # Append character to list
                if (printList != ""):
                    printList = printList + " " + outline
                else:
                    printList = printList + outline
            else:
                innerList.append(fill) # use fill character
                printList = printList + " " + fill
        print(printList)

main() # End program
