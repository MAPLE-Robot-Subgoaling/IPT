def main():
    height = int(input("Please input a positive integer to represent the starting height of the hailstone: "))
    while(height!=1): #will first check if the hail is at 1, because this ends the program essentially
        print("Hail height is", height) #the print statment is before the if statments so that the users hail hieght is also displayed
        if(height%2 == 0): # checks if the number is even
            height = height//2 # interger division is used so that the ouputs are ints and not decimals/floats
        else:
            height = (height*3)+1
    print("The hail stopped at height", height)
main()
