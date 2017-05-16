
def main():

    height=int(input("Please enter the height of the box :"))
    width=int(input("Please enter the width of the box :"))

    fill=input("Please enter the symbol that will fill the box :")
    fill= fill*(width-2)

    inpOutline=input("Please enter the symbol that will outline the box :")
    outline= width*inpOutline
    print(outline)
    for i in range (2, height):

        newOutline=outline[1]
        print (inpOutline+fill+inpOutline)

    if height >1:
        print (outline)

main ()
