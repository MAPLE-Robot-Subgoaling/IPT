
def main():
    STOP = 1
    height = int(input("Please enter the starting height of the hailstone: "))
    while (height <=0):
        print("The starting height must be a positive number greater than 0")
        height = int(input(" Please enter the starting height of the hailstone: "))
    while (height != STOP):
        print ("Hail is currently at height", height)
        heightMOD = height % 2
        if (heightMOD == 0):
            height = height // 2
        elif (heightMOD == 1):
            height = (height * 3) + 1
    print ("Hail stopped at height", STOP)



main()
