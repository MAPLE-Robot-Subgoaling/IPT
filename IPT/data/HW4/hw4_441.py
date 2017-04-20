

def main():
    EVEN_CHECKER = 2

    
    startingHeight = int(input("Please enter the starting height of the hailstone: "))
    currentHeight = startingHeight
    
    while currentHeight != 1:

        print("Hail is currently at height", currentHeight)
        
        result = int(currentHeight / EVEN_CHECKER)
        result = result*EVEN_CHECKER
        result = currentHeight - result
        
        if result == 0:
            currentHeight = currentHeight // 2
        else:
            currentHeight = (currentHeight * 3) + 1


    print("Hail stopped at height", currentHeight)



main()
