
END = 1
def main():

    height = int(input("Please enter the starting height of the hailstone: "))
    
    while(height != END):
        print("Hail is currently at height",height)
        
        evenOdd = (height % 2)

        if(evenOdd == 0):
            height = int(height / 2)

        elif(evenOdd == 1):
            height =int((height * 3) + 1)
    
    print("Hail stopped at height", END)



main()
