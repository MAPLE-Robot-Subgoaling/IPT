def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symOut = input("Please enter a symbol for the bow ouline: ")
    symFill = input("Please enter a symbol for the box fill: ")
    for num in range(height):
        prnOut = ""
        for num2 in range(width):
            if num == 0 or num == height - 1:
                prnOut += symOut
            else:
                if num2 == 0 or num2 == width - 1:
                    temp = str(symOut)
                else:
                    temp = str(symFill)
                prnOut += temp
        print(prnOut)
main()
