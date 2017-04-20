
def main():

    width= int(input("Please enter the width of the box: "))
    height= int(input("Please enter the height of the box: "))
    symOut= input("Please enter a symbol for the box outline: ")
    symIn= input("Please enter a symbol for the box fill: ")

    symOutStr= symOut*width
    symInOutStr= symOut + symIn*(width - 2) + symOut
    
    if height > 1:
        print(symOutStr)
        for x in range(height - 2):
            print(symInOutStr)
        print(symOutStr)
    if height <= 1:
        print(symOutStr)

main()
