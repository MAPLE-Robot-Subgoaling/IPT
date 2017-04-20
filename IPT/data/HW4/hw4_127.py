
def main():

    hs_start= int(input("what is the starting height of the hailston: "))
    while hs_start <= 0:
        print("Your interger must be postive")
        hs_start= int(input("Please enter the starting height of the hail: "))
    print("Current height of the hail is", hs_start) 
    while hs_start >1:
        if hs_start == 1:
            print("The hail has stopped falling at", hs_start)
        elif hs_start%2 == 0:
            hs_start= int(hs_start/2)
            print("The current height of the hail is", hs_start)
        else :
            hs_start= int((hs_start*3)+1)
            print("The current height of the hail is", hs_start)
main()
