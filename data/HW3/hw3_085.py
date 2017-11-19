def main():
    temp=float(input("Enter a temperature: "))
    kc=input("Is that in Kelvin K or Celcius C? ")
    if kc=="C":
               if temp<=0:
                   print("At this temperature, water is soild.")
               elif temp>=100:
                   print("At this temperature, water is gas.")
               else:
                   print("At this temperature, water is liquid.")
    elif kc=="K":
               if temp<=273.15:
                   print("At this temperature, water is soild.")
               elif temp>=373.15:
                   print("At this temperature, water is gas.")
               else:
                   print("At this temperature, water is liquid.")
    else:
        print("Wrong input. Restart and try again.")
main()
