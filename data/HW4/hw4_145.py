STOP_HEIGHT = 1
EVEN_HEIGHT = 2
ODD_HEIGHT = 3 
ODD_HEIGHT_CONSTANT = 1
def main():
    input_height = int(input("Please enter a positive integer start value of the hailstone: "))
    while input_height < 0:
        print("enter a positive integer")
        input_height = int(input("Please enter a positive integer start value of the hailstone: "))
    print("Hail is currently at height",input_height)
    while input_height != STOP_HEIGHT:
        if (input_height % 2) == 0:
            input_height = input_height //  EVEN_HEIGHT
            if input_height != STOP_HEIGHT:
                print("Hail is currently at height",input_height)
            else:
                print("Hail stopped at",input_height)
        else:
            input_height = (input_height * ODD_HEIGHT) + ODD_HEIGHT_CONSTANT
            if input_height != STOP_HEIGHT:
                print("Hail is currently at height",input_height)
            else:
                print("Hail stopped at",input_height)
main()
