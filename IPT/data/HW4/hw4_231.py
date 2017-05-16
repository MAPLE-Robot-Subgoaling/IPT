
def main():
    height = 0
    STOP_HEIGHT = 1     #The height to stop the simulation at
    numberType = ""     #Will be used to store whether the current Height is odd or even
    ONE = 1
    TWO = 2
    THREE = 3
    height = int(input("What height is the hailstone at: "))
    while height != 1:
        print("THe hailstone is currently at height:", height) 
        if height % TWO == 0:                              #These if else statements
            numberType = "even"                          #Determine if the height 
        else:                                            #is even or odd.
            numberType = "odd"

        if numberType == "even":
            height = height // TWO
        else:
            height = (height * THREE) + ONE
    print("The hailstone has stopped at height", height )

main()
