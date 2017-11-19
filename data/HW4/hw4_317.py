def main ():
    height = int(input('Please enter the starting height of the hailstone: '))
    print('Hail is currently at height', height)
    while height != 1 : 
        if(height % 2 == 0):
            height = height//2
            if height==1:
                print('The hail stopped at height 1')
            else:
                print('Hail is currently at height' , height)
        elif(height % 2 == 1):
            height = (height*3) + 1
            if height==1:
                print('The hail stopped at height 1')
            else:
                print('Hail is currently at height' , height)
main()
