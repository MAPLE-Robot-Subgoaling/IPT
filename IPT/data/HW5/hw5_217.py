
def main():
    
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    
    for i in range(0, height):
        if i == 0:
            print(width * outline)
        elif i != 0 and i != height:
            print(outline + (fill * (width - 2)) + outline) 
            
        if i == (height - 1) and (i != 0) :
           print(width * outline)
    
  
main()
