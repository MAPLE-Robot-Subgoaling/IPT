
def main():
    width  = int(input("Please enter the width of the box: "))
    length = int(input("Please enter the height of the box: "))
    outer  = input("Please enter a symbol for the box outline: ")
    inner  = input("Please enter a symbol for the box fill: ")

    inwid=width-2
    inlen=length-2

    print(outer*width) #prints the first line of the box

    if length > 2:
        for n in range(inlen):
            if width > 1:
                print(outer + (inner * inwid) + outer)
            else:
                print(outer)
    if length >= 2:
        print(outer * width)



main()
