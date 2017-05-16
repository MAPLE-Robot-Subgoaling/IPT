
def main():
    width=int(input('Please enter the width of the box: '))
    height=int(input('Please enter the height of the box: '))
    out=input('Please enter the symbol for the box outline: ')
    fill=input('Please enter the symbol for the box fill: ')
    row_count=1
    col_count=1
    while row_count<=height:
        while col_count<=width:
            if row_count==1 or row_count==height or col_count==1 or col_count==width:
                print(out, end='')
                col_count=col_count+1
            else:
                print(fill, end='')
                col_count=col_count+1

        col_count=1
        print(' ')
        row_count=row_count+1

main()
