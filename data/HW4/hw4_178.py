def main():
    height=int(input("Please enter the starting height of the hailstone: "))
    if height==1:
        print("The hailstone is at a height of ",height)
    else:
        print("The hailstone is currently at a height of ",height)
        while height!=1:
            if(height%2==0):
                height=int(height/2)
                if(height!=1):
                    print("The hailstone is currently at a height of ",height)
            elif(height%2==1):
                height=height*3+1
                if(height!=1):
                    print("The hailstone is currently at a height of ",height)
        print("The hailstone stopped at a height of ",height)
main()
