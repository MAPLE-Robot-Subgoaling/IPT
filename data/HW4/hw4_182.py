File Edit Options Buffers Tools Python Help                                                  
def main():
    heightValue = int(input("Please enter the starting height of the hailstone:"))
    while (heightValue %  2 != 0):
        heightValue = (heightValue * 3) + 1
        print(heightValue)
        while (heightValue %  2 ==  0):
            heightValue = heightValue / 2
            print(heightValue)
    else : 
        print("1")
main()
