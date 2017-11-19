def main():
     userWidth = int(input("Please enter the width of the box: "))
     userHeight = int(input("Please enter the height of the box:  "))
     userOutline = input("Please enter a symbol for the box outline: ")
     userFill = input("Please enter a symbol for the box fill")
     for row in range(userHeight) :
         if row == 0 or row == (userHeight - 1):
             print(userOutline *  userWidth)
         else:
                 print(userOutline + (userFill) * (userWidth - 2) + userOutline)
main()
