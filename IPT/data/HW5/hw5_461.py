
def main():
    width = int(input("Please enter the width of the box: "))
    heigh = int(input("Please enter the height of the box: "))
    outline = input("Please enter the outlining symbol: ")
    content = input("Please enter the inside symbol: ")
    
    for n in range(heigh):
            if n != 0 and n != (heigh - 1):
                print(outline + content*(width-2) + outline)
            else:    
                print(outline*width)
main()
