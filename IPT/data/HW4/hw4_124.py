def main():

 height= int(input("Please enter the starting height of hailstone: "))

 while height!=1:
    print("Hail is currently at height", height)
    if height%2 == 1:
       height=int(height*3+1)
    elif height%2 == 0:
       height= int(height/2)
 print("Hail stopped at height", height)

main()
