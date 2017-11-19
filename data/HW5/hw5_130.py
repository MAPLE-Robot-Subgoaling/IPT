def main():
    width=(int)(input("Please enter the width of the box:"))
    height=(int)(input("Please enter the height of the box:"))
    outline=(input("Please enter a symbol for the box outline:"))
    fill=(input("Please enter a symbol for the box fill:"))
    top_bottom=""
    middle=""
    for x in range(0,width+1):
        top_bottom=top_bottom+outline
    for x in range(0,width-2):
        middle=middle+fill
        print(middle)
        print(x)
    middle=outline+middle+outline
    print(top_bottom)
    for x in range(0,height-2):
        print(middle)
    print(top_bottom)
main()