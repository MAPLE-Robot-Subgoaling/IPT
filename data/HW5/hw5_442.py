def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outside = input("Please enter a symbol for the box outline: ")
    inside = input("Please enter a symbol for the box fill: ")
    filling = [inside]*(width - 2) 
    buns = [outside]*width 
    wall = [outside] 
    print(buns)
    for n in range(height - 2): 
        print(wall + filling + wall)
    if width and height != 1: 
        print(buns)
main()
