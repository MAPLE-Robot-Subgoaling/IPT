0
def main():
    height=int(input('Please enter starting height of the hailstone: '))
    while height!=1:
        print('The hail is currently at the height ',int(height))
        if height%2==0:
            height=height/2
        else:
            height=(height*3)+1
    print('Hail stopped at height 1')
main()
