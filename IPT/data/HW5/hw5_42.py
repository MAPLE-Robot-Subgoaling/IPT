
def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")

    border = outline * width
    center = outline
    for i in range(width - 1):
        if i != width - 2:
            center = center + fill
        else:
            center = center + outline
    
    for j in range(height):
        if j == 0 or j == height - 1:
            print(border)
        else:
            print(center)

main()
