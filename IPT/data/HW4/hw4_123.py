
def main():
    
    hail=float(input("Please enter the starting height of the hailstone:"))
    while hail!=1:
         if (hail % 2)== 0:
             hail= int(hail/2)
             print("Hail is currently at height", hail)
         elif (hail % 2)!=0:
             hail= (hail*3)+1
             print("Hail is currently at height",hail)
    if (hail)==1:
         print("Hail stopped at height 1")

main()
