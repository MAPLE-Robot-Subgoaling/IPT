
def main():
    
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outside = input("Please enter a symbol for the box outline: ")
    inside = input("Please enter a symbol for the box fill: ")
    filling = [inside]*(width - 2) #list for inside the box
    buns = [outside]*width #list for top and bottom walls of the box
    wall = [outside] #walls of the box

    print(buns)
    for n in range(height - 2): #loops inner box
        print(wall + filling + wall)
    if width and height != 1: #proceeds if user doesn't input a 1 x 1 box
        print(buns)

main()

