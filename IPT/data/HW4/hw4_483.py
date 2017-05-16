
def main():

    h = int(input("Please enter the starting height of the hailston: "))
    
    while (h != 1):
        print("Hail is currently at height ", h)
        if ((h % 2) == 0):
            h = h//2
        elif  ((h % 2) != 0):
            h = (h*3)+1
    print("Hail stopped at height ",h)

main()
                
