
def main():
     num = int(input("Please enter a number: "))
              
     while (num < 1):
         print("Please enter a whole number greater than 0.")
         num = int(input("Enter a new number: "))

     if (num == 1):
         print("Your height has reached 1!")
     elif (num > 1):
         while (num > 1) and (num % 2 == 0):
             num = num / 2
             print("The height has reached ", num)
             while (num > 1) and (num % 2 == 1):
                 num = (num * 3) + 1
                 print("The height has reached ", num)
         while (num > 1) and (num % 2 == 1):
              num = (num * 3) + 1
              print("The height has reached ", num)
              while (num > 1) and (num % 2 ==0):
                   num = num / 2
                   print("The height has reached ", num)
         print("Your height has reached ", num, "!")
     else:
         print("Somethings not right here, check your code")
main()
