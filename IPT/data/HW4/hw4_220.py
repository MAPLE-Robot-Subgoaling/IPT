

def main():
    size=(int)(input('Please enter the starting height of the hailstones'))
    while(size!=1):
        print("Hail is currently at height",size)
        if size%2==0:
            size=(int)(size/2)
        else:
            size=int(size*3)+1

main()