

def main():
 width = int(input("Please enter the width of the box: "))
 height = int(input("Please enter the height of the box: "))
 symbolOut = str(input("Please enter a symbol for the box outline: "))
 symbolIn = str(input("Please enter a symbol for the box fill: "))
 print(symbolOut * width)
 for i in (height - 2):
     print(symbolOut + ((width -2) * symbolIn) + symbolOut)

 print(symbolOut * width)

main()
