def main():
    PROMPT_WIDTH = "Please enter the width of the box: " 
    PROMPT_HEIGHT = "Please enter the height of the box: " 
    PROMPT_OUTLINE = "Please enter a symbol for the box outline: " 
    PROMPT_FILL = "Please enter a symbol for the box fill: " 
    width = int(input(PROMPT_WIDTH))
    height = int(input(PROMPT_HEIGHT))
    outline = input(PROMPT_OUTLINE)
    fill = input(PROMPT_FILL)
    for i in range(0, height):
        if (i == 0 or i == height - 1):
            line = outline * width
        else: 
            line = outline + fill * (width-2) + outline 
        print(line)
main()
