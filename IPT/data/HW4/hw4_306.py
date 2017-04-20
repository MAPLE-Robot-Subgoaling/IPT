
def main():

    height = int(input("Please enter the starting height of the hailstone: "))
    print("Hail is currently ate height",height)

    while height > 1:

        if height % 2 == 0 :
            
            if height > 2:
                height = height // 2
                print("Hail is currently at height",height)
                
            elif height >= 2:
                height = height // 2

        elif height % 2 != 0:
            height = (height * 3) + 1
            print("Hail is currently at height",height)
    else:
        print("Hail stopped at height 1")
main()

