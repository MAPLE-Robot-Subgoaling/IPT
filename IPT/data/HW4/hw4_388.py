
def main():

    numberinput = int(input("Please input a postive number with that: "))
    
    while numberinput !=1:
        if numberinput%2 == 0:
            numberinput=numberinput/2 
            print("Hail is currently at height",numberinput,"")
        elif numberinput !=0:
            numberinput=((numberinput*3)+1)
            print("Hail is currently at height",numberinput,"")
    print("Hail is currently at height",numberinput,"")











main()
