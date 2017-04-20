
def main():

    height = int(input("Please enter a height:"))

    while (height > 1):
        if (height % 2 == 0):
            print ("Height is currently at", height)
            height = height / 2
        else:
            print ("Height is currently at", height)
            height = height * 3 + 1
    print ("Hail stopped at height 1.")
    

    







main()
