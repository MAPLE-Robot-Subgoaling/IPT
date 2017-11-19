def main():
    height = int(input("Please enter an integer: "))
    while height != 1:
        print("Hail is currently at height",height)  
        if height % 2 == 0:
            height = int( height / 2)
        elif height % 2 != 0: 
            height = int(( height * 3 ) + 1)
    print("Hail stopped at height",height)
main()
