
def main():

    width = int(input("Enter width: "))
    height = int(input("Enter height: "))
    outline = input("Enter symbol for outline: ")
    fill = input("Enter symbol for fill: ")

    box = [None]*height
    
    n = 0
    for i in box:
        box[n] = outline * width
        n = n + 1

    for i in range(1, height-1):
        box[i] = outline + fill * (width - 2)
        if width >= 2:
            box[i] = box[i] + outline
    
    for i in box:
        print(i)


main()
print()
