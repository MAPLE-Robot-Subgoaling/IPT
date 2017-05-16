
def main():
    
    hail = int(float(input("Please enter a positive integer: ")))

    print("Hail is currently at "+ str(int(hail)))

    while hail != 1:
        
        if hail % 2 == 0:
            hail = hail /2
        else:
            hail = (hail*3)+1
        print ("Hail is currently at " + str(int(hail)))
    print ("Hail has stopped at height 1.")



main()
