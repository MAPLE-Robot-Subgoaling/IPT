def box():
    width = int(input("How wide do you want your box to be?"))
    height = int(input("How high do you want your box to be?"))
    outline = input("What symbol do you want your box to be oulined with?")
    fill = input("How would you like the box to be filled?")
    for i in range(0,width):
        if i == 0 or i == width:
           print(width * outline)
    for j in range(0, (height-2)):
            if j == 0 and j == height:
                print(outline)
            else:
                print(fill* width)
    print(width * outline) 
def main():
    box()
main()
