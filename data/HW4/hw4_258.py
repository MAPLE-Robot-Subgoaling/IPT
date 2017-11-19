def main():
    height = int(input("What is the current height of the hail?"))
    while height % 2 == 0:
        height = height / 2
        print("Hail is currently at height" , height)    
        while height % 2 == 1:
            height = (3 * height) + 1
            print("Hail is currently at height", height)
    if(height == 1):
        print("Hail stopped at height 1")
main()
