
def main():

    width = int(input("please enter the width of the box: "))
    height = int(input("please enter the height of the box: "))
    outline = input("please enter a symbol for the box outline: ")
    fill = input("please enter a symbol for the box fill: ")
    temp = ""

    endRow = list(outline*width)
    midRow = list((outline) + (fill*(width-2)) + (outline))
    
    for i in endRow:
        temp = temp + i
    print(temp)
    temp = ""

    for num in range(0,height-2):
        for i in midRow:
             temp = temp + i
        print(temp)
        temp = ""

    for i in endRow:
        temp = temp + i
    print(temp)
 

main()
