def main():
    print("Pleas enter a positive integer.")
    height= input("pleas enter the starting height of the hailstone: ")
    height= int(height)
    while(height!= 1):
        print(" Hail is currently at height ", height)
        if (height % 2== 0):
            height= height//2 
        else:
            height = (height*3)+1
    print(" Hail stopped at height 1")
main()
