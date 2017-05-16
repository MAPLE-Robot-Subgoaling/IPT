

def main():

    
    height = int(input("Please enter the starting height of the hailstone: "))
    evenNum = (height % 2)
    while height != 1:
        print("Hail is currently at height",height)
        if evenNum == 0:
            height = height // 2
            evenNum = (height % 2)
        elif evenNum != 0:
            height = (height*3 + 1)
            evenNum = (height % 2)
    print("Hail stopped at height",height)
main()
