
def main():
    width = int(input("Please enter the width of the box: ")) # Prompt user for the width of the box
    height = int(input("Please enter the height of the box: ")) # Prompt user for the height of the box
    outline = input("Please enter a symbol for the box outline: ") # Prompt user for the symbol that will make up the box's outline
    fill = input("Please enter a symbol for the box fill: ") # Prompt user for the content that will fill the interior of the box
    BUFFER = 2 # When creating the fill for the box, set this much aside for the border
    for i in range(height):
        print((outline + fill * (width-BUFFER) + (outline if width > 1 else "")) if i not in [0, height-1] else outline * width) # Print the box
main()