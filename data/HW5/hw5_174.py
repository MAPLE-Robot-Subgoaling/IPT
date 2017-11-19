def main():
    width = int(input("What is the width? "))
    height = int(input("What is the height? "))
    outline = input("What is the box outline? ")
    fill = input("What is the box fill? ")
    for i in range(height):
        if i == 0 or i == (height-1):
            print(outline * width)
        else:
            print(outline + (fill*(width-2)) + outline)
main()
