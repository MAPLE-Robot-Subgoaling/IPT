

def main():

    boxWidth = int(input("Please enter the width of the box: "))
    boxHeight = int(input("Please enter the height of the box: "))
    symOne = input("Please enter a symbol for the box outline: ")
    symTwo = input("Please enter a symbol for the box fill: ")
    counter = 0
    for n in range(0, boxHeight):
        if (counter == 0 or counter == boxHeight - 1):
            print(symOne * boxWidth)
            counter = counter + 1
        else:
            counter = counter + 1
            print(symOne + (symTwo * (boxWidth - 2)) + symOne)

main()
