def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    def topBottom():
        row = outline * width
        print(row)
    topBottom()
    def inside():
        for i in range(1, height):
            rows = fill * (width - 2)
            insideRow = outline + rows + outline
            print(insideRow)
    inside()
    topBottom()
main()
