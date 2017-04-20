

def main():

    width=int(input("Please enter the width of the box:"))
    height=int(input("Please enter the height of the box:"))
    
    symbol_o=str(input("Please enter a symbol for the box outline:"))
    symbol_f=str(input("Please enter a symbol for the box fill:"))

    ex=list(range(0, width))
    up=list(range(0, height))

    put=symbol_o*width
    
    print(put)
    
    for i in range(0,height-2):
        across=width-2
        out=across*symbol_f
        print(symbol_o,out,symbol_o)
    if height>=2:
        print(put)
main()
