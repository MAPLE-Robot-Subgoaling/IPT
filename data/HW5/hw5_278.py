def main():
    width=int(input("Please enter the width of the box:"))
    height=int(input("Please enter the height of the box:"))
    outline=input("Please enter a symbol for the box outline:")
    fill=input("Please enter a symbol for the box fill:")
    for n in range(height-1):
        if n==0 or n==range(height-1):
            print(width*outline)
        else:
            print(outline+((width-2)*fill)+outline)
    if height>1:
        print(width*outline)
main()
