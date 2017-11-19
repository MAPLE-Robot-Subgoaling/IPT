def main():
    width = int(input(" please enter the width of the box"))
    height = int(input("Please enter the height of the box"))
    symbolO = input("please enter a symbol for the box outline")
    symbolF = input("please enter a symbol for the box fill")
    print((width) * symbolO)
    for box in ((height-2)*symbolO):
        box = box + ((width -2) * symbolF) + symbolO
        print(box)
    if width != 1 and height != 1:
        print((width) * symbolO)
main()
