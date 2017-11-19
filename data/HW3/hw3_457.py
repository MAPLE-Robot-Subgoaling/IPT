def main() :
    temperature = float(input("Please enter the temperature: "))
    tempScale = input("Please enter 'C' for Celsius or 'K' for Kelvin: ")
    print()
    if tempScale == 'C' :
       if temperature <= 32 :
          print("At this temperature, water is a solid")
       elif temperature > 32 and temperature < 100 :
          print("At this temperature, water is a liquid")
       elif temperature >= 100 :
          print("At this temperature, water is a gas")
    elif tempScale == 'K' :
         if temperature <= 273.16 :
            print("At this temperature, water is a solid")
         elif temperature > 273.17 and temperature < 373.16 :
            print("At this temperature, water is a liquid")
         elif temperature >= 373.16 : 
            print("At this temperature, water is a gas")
main()
