
def main():

    width   =  int(input("Please enter the width of the box: "))
    height  =  int(input("Please enter the width of the box: "))
    outline =  input("Please enter a symbol for the box outline: ")
    boxFill =  input("Pleae enter a symbol for the box fill: ")
    print(width * outline)
    for n in range(height): 
        lengthFill = width - 2
        print(outline + (lengthFill * boxFill) + outline) 
    print(width * outline)
main()
