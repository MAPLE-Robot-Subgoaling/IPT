

def main():
    height = int(input("Please enter the starting height of the hailston\
e: "))
    while height != 1: 
        print("Hail is currently at height", height)
        num = height % 2
        if num == 1:
            height = (height * 3) + 1
        else:
            height = (height / 2)
            
    print("Hail stopped at 1")
main()







