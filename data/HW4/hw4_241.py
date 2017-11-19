def main():
    num = int(input("Please enter any positive number : "))
    while num > 1:
        if num == 1:
            print ("Hail stopped at 1")
        elif num % 2 == 0:
            num = int(num/2)
            print ("Hail is currently at :", num)
        elif num % 2 == 1:
            num = int((num * 3)+ 1)
            print ("Hail is currently at :",num)
main()  
