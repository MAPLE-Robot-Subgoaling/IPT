def main():
   Temperature =  float(input(" Please enter the temperature "))
   Scale =  input(" Please enter 'C' for celcius, or 'K' for Kelvin ")
   if Scale == 'C':
      if Temperature <= 0:
         print(" At this temperature, water is a solid")
      if Temperature >= 100:
         print(" At this temperature, water is a gas")
      if Temperature > 0 and Temperature < 100:
         print(" At this temperature, water is a liquid")
   if Scale == 'K':
      if Temperature <= 273.15:
         print(" At this temperature, water is a solid")
      if Temperature >= 373.15:
         print(" At this temperature, water is a gas")
      if Temperature > 273.15 and Temperature < 373.15:
         print(" At this themperature, water is a liquid")
main()
