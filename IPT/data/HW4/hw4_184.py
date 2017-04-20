
def main():
    
    Start = int(input("please enter the starting height of the hailstone"))
    
    while Start > 1:
        if Start%2 != 0:
            Start = Start*3 + 1
            print("Hail is currently at height ", Start)
        elif Start%2 == 0:
            Start = Start//2
            print("Hail is currently at height ", Start)
        

    print("The hail stopped at height 1")

main()
