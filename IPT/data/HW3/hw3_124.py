
def main():
 temp =float(input("Please enter the temperature: "))
 state= input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
 if state=="C":
    if temp<=0:
        print("At this temperature, water is a solid (frozen)")
    elif temp>100:
        print("At this temperature, water is a gas")
    else:
        print("At this temperature, water is a liquid")
 elif state=="K":
    if temp<=273.15:
      print("At this temperature, water is a solid (frozen)")
    elif temp>373.15:
      print("At this temperature, water is a gas")
    else:
      print("At this temperature, water is a liquid") 
 else:
    print("Try again")
main()
