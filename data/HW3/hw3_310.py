def main():
    temp= float(input("Enter the value of temperature:"))
    scale = input("Enter C for celsius and K for Kelvin:")
    if(scale =='C'):
        if(temp>0 and temp<100):
           print(" It is liquid")
        elif(temp<=0):
           print("It is solid")
        else:
           print("It is gas")
    else:
         if(temp<=273):
           print("It is solid")
         elif(temp>273 and temp<373):
           print("It is liquid")
         else:
           print("It is gas")
main()
