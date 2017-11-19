def main():
    height = int(input("Please enter the height of the box: "))
    width = int(input("Please enter the width of the box: "))
    outlined = input("Please enter a symbol for the box's outline: ")
    filler = input("Please enter a symbol for the box's filling: ")
    MIN=1
    print(width*outlined)
    for n in range(0, height - 2, 1):
        print(outlined + ((width - 2) * filler) + outlined)
    if height > MIN:
        print(width*outlined)
main()
