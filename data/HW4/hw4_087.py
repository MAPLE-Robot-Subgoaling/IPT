def main():
    height = int(input("Please input the starting height of the hailstone: "))
    hailStop = 1 
    evenOdd = height % 2 
    evenHeight = 0 
    even = height // 2 
    odd = (height * 3) + 1 
    if height == hailStop: 
        print("The hail stopped at height 1") 
    while height != hailStop: 
        if evenOdd == evenHeight: 
            even = height // 2 
            height = even 
            evenOdd = height % 2 
            if height == hailStop: 
                print("Hail stopped at height 1")
            else: 
                print("Hail is currently at height", height) 
        elif evenOdd != evenHeight: 
            odd = (height * 3) + 1 
            height = odd 
            evenOdd = height % 2 
            print("Hail is currently at height", height) 
main()    
