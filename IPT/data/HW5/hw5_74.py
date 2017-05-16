
def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    Symbol1 = input("Please enter a symbol for the box outline: ")
    Symbol2 = input("Pleas enter a symbol for the box fill: ")
    for n in range(height):
        if n == 0 or n == height-1 :
            print(Symbol1*width)
        else: 
            print(Symbol1 + (Symbol2*(width-2) + Symbol1))
main()


