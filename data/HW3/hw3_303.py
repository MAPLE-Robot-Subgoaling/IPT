def main():
    userNumber = float(input("Please enter the temperature: "))
    userScale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if userScale == 'K':
       if userNumber <= 273.15:
           print("At this temperature, water is a (frozen) solid.")
       elif userNumber >= 373.15:
           print("At this temperature, water is a gas.")
       else :
           print("At this temperature, water is a liquid.")
    else :
       if userNumber <= 0:
           print("At this temperature, water is a (frozen) solid.")
       elif userNumber >= 100:
           print("At this temperature, water is a gas.")
       else :
           print("At this temperature, water is a liquid.")
main()
