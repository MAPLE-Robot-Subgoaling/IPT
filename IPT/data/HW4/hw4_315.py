
def main():
    height = int(input("Please enter the starting height of the hailstone: "))
    
    currentHeight = height
    SENTINEL = 1
    
    while currentHeight != SENTINEL:
        print("Hail is currently at height", currentHeight)
        
        if currentHeight % 2 == 0: 
            currentHeight = currentHeight//2
        else:
            currentHeight = (currentHeight * 3) + 1
    
    print("Hail stopped at height", currentHeight)




main()
