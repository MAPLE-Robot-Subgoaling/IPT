

def main():
    num = int(input("Please enter an integer: "))
    user_num = num
    
    while num != 1 or num % 2 == 0 :
        user_num = (num)

        if num % 2 == 0:
            num = num / 2
            print ("hail is currenlty at the height", +num)

        else:
            num = num*3+1
            print ("hail is currenlty at the height", +num)

    print ("Hail stopped at height", +num)

    
main()
