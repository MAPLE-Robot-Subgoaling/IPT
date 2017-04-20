

def main():

    width = int(input("Pleast enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    filling = input("Please enter a symbol for the box to fill: ")
    
    print(width * outline)
    for h in range(height - 2):
        print(outline + filling * (width - 2) + outline)
    if height > 1:
        print(outline * width)
        
main()
