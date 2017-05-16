
def main():
    width=int(input("Enter the width of the box "))
    height=int(input("Enter the height of the box "))
    symbol1=input("Enter the outer symbol of the box ")
    symbol2=input("Enter the inner symbol of the box ")
    for n in range(height):
        if n==0 or n==height-1:
            print(symbol1*width)
        else:
            print(symbol1+(symbol2*(width-2))+symbol1)
main()
