
def main():

    w = int(input("Please enter the width of the box: "))
    l = int(input("Please enter the height of the box: "))

    symO = input("Please enter the symbol for the box outline: ")
    symI = input("Please enter the symbol for the box fill: ")

    line = ""
    line2 = symO

    for x in range(0, w):
        line += symO
    print (line)

    for x in range (0, w-2):
        line2 += symI

    line2 += symO

    for x in range(0, l-2):
        print (line2)

    print (line)

main()
