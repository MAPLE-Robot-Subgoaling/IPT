
def main():
    curHeight = -1
    while curHeight < 0:
        curHeight = int(input("Please enter the starting height of the hailstone: "))
    
    while curHeight != 1:
        print("Hail is currently at height",int(curHeight))
        if curHeight%2 == 0:
            curHeight = curHeight/2
        else:
            curHeight = curHeight*3+1
        
    print("Hail stopped at height 1")
    
main()
