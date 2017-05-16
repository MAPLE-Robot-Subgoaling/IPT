
def main():
    height = int(input("Please enter the starting height of the hailstorm: "))
    
    while height != 1:
        if height % 2 == 0:
            print(height // 2)
            
        elif height % 2 != 0:
            height = (height *3) +1
            print(height) 
main()
