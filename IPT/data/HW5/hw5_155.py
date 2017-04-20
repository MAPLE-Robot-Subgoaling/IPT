
def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = str(input("Please enter a symbol for the box outline: "))
    fill =  str(input("Please enter a symbol for the box fill: "))
    
    
    for s in range(0, height):
        if s == 0 or s == height -1:
            print(outline*width)
        else:
            print(outline + fill * (width - 2) + outline)
    

main()
