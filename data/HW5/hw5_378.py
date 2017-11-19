def main():
    width = int(input("Please enter the width of the box: ")) 
    height = int(input("Please enter the height of the box: ")) 
    outline = input("Please enter a symbol for the box outline: ") 
    fill = input("Please enter a symbol for the box fill: ") 
    BUFFER = 2 
    for i in range(height):
        print((outline + fill * (width-BUFFER) + (outline if width > 1 else "")) if i not in [0, height-1] else outline * width) 
main()