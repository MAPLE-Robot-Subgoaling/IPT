
def main():

    hailstone = int(input("Please enter the starting height of the hailstone: "))
   
    if hailstone == 1:
        print("Hail stopped at height 1")

    while hailstone % 2 == 1 and hailstone > 2: 
        print("Hail is currently at height" , hailstone)
        hailstone = (hailstone * 3) + 1            
  
    while hailstone % 2 == 0:
        print("Hail is currently at height" , hailstone)
        hailstone = hailstone // 2
        if hailstone == 1:
            print("Hail stopped at height 1")
        elif hailstone % 2 == 1:
            print("Hail is currently at height" , hailstone)
            hailstone = (hailstone * 3) + 1

main()
