def main():
    width= int(input("What is the width of the box? "))
    height= int(input("What is the height of the box? "))
    outer_symbol= input("What symbol do you want to use to outline the box? ")
    inner_symbol= input("What symbol do you want to use to fill the box? ")
    for i in range(height):
        if i == 0 or i == height -1:
            print( outer_symbol*width)
        else:
            print(outer_symbol+(inner_symbol *(width- 2))+outer_symbol)
main()
