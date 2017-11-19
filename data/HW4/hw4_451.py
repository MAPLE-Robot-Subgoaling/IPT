def main():
    height = int(input("Please enter a positive integer that is greater than 1: "))
    while height != 1: 
        if height % 2 == 0:
            height = height / 2
            print("The height of the hail is", height)
        elif height % 2 == 1: 
            height = (height * 3) + 1
            print("The height of the hail is", height)
    if height == 1:
        print("The stopped height of the hail is", height)
        print("Thank you for your input!")
main()
