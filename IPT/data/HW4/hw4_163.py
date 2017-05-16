
def main():
    
    hailstone = int(input("Please enter height of hailstone: "))
    print("Hail is currently at height " , hailstone , " ")
    while hailstone > 2:
        if hailstone % 2 == 0:
          hailstone = hailstone // 2
          print("Hail is currently at height " , hailstone , " ")
        elif hailstone % 2 != 0:
          hailstone = hailstone * 3 +1
          print("Hail is currently at height " , hailstone  , " ")
        
    print("Hail stopped at height 1 ")

            
main()
