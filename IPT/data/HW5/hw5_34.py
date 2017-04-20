
def main():

    width = int(input("Please enter the width of your box: "))
    height = int(input("Please enter the height of your box: "))
    outside = input("Please enter the symbol you'd like as the outline your box: ")
    inside = input("Please enter the symbol you want to fill your box: ")
 
    if height != 1 and width != 1:
        for x in range(height):
            if x == 0:
                print (outside * width)
            if 0 < x < height:
                print (outside + inside * (width - 2) + outside)
            if x == height - 1:
                print (outside * width)
    else:
        print(outside)

main()
        
