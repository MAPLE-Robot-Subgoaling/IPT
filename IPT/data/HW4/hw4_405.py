
def main():
    
    END_HGHT = 1
    EVEN_HGHT = 0
    DIV_NUM = 2
    MULT_NUM = 3
    
    startHeight = int(input("Enter the starting height of the hailstone: "))
    modHeight = int(startHeight % DIV_NUM)

    print("Hail is currently at height", startHeight)

    while (modHeight == END_HGHT and startHeight > END_HGHT) or (modHeight == EVEN_HGHT and startHeight >  END_HGHT):
        
        if modHeight == END_HGHT:
            startHeight = (startHeight * MULT_NUM) + END_HGHT
        
        elif modHeight == EVEN_HGHT:
            startHeight = startHeight // DIV_NUM
        
        print("Hail is currently at height", startHeight)
        modHeight = int(startHeight % DIV_NUM)

    print("Hail stopped at height", END_HGHT)

main()



