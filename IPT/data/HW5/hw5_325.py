
def main():
    
    width = float(input("Please enter the width of the box: "))
    height = float(input("Please enter the height of the box: "))
    symbolPerim = input("Please enter a symbol for the box outline: ")
    symbolFill = input("Please enter a symbol for the box fill: ")
    for h in range (0,int(height)):
        if h == 0 or h == height-1:
            print ( symbolPerim * int(width) )
        else:
            print (symbolPerim + (symbolFill*(int(width-2)))+ symbolPerim)
main()
