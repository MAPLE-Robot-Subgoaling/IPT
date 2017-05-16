


def main ():

    width= int(input("Please enter the width of the box: "))
    height= int(input("Please enter the height of the box: "))
    out= input("Please enter a symbol for the box outline: ")
    fill= input("Please enter a symbol for the box fill: ")
   
    for outBox in range(height):
        if outBox == 0 or outBox == (height-1):
            print("",(out* width))

        else:
            print("", (out + (fill*(width-2))+ out))
        

main()
