def main():
    width = int(input('please Enter the width: '))
    range(width)
    hieght = int(input("please Enter the hieght of the box: "))
    range(hieght)
    sym = input('please enter symbole: ')
    in_sym = input('please enter a sym to fill the box: ')
    for i in range(hieght):
        if( i == 0 or i == hieght-1):
            print(width* sym , end='')
        else :
            print(sym , end="");
            print((width-2)*in_sym, end="")
            print(sym, end="")
        print('')
main()
