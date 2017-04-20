def main():
    startingHeight=int(input("Please enter the starting height of the hailstone:"))
    while startingHeight>1:
        print("Hail is currently at Height",startingHeight)
        if startingHeight % 2==0:
            startingHeight=startingHeight/2
        elif startingHeight % 2==1:
            startingHeight= (startingHeight*3)+1
    print("Hail stopped at height",startingHeight)
main()            
            
