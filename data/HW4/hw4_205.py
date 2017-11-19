def main():
    height = int(input("Please input a positive integer to represent the starting height of the hailstone: "))
    while(height!=1): 
        print("Hail height is", height) 
        if(height%2 == 0): 
            height = height//2 
        else:
            height = (height*3)+1
    print("The hail stopped at height", height)
main()
