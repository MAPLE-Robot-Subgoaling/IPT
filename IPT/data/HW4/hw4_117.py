
def main():
    height=int(input("Please enter the height of the hail: "))
    if height <= 1:
        print("OOPS! You quit the program, gotta be greater than 1")
    while height > 1:
        even = height % 2 
        if even == 0:
            if height >= 1:
                print("The current height is ",height)
                height=height//2
        elif even != 0:
            if height >= 1:
                print("The current height is ", height)
                height=height*3+1
            
    print("The hail stopped at " ,height)
main()
