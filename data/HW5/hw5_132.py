def main():
    w=int(input("Enter the width: "))
    h=int(input("Enter the height: "))
    fill=input("Enter symbol for the fill: ")
    outline=input("Enter the symbol for the outline: ")
    top=""
    for i in range(0,w):
        top=str(top+outline)
    print(top)
    inner=""
    for i in range(1,h-1):
        for u in range(0,w):
           if(u==0 or u==w-1):
               inner=str(inner+outline)
           else:
               inner=str(inner+fill)
        print(inner)
        inner=""
    print(top)
main()
