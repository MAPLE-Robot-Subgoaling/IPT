def main():
   temp = float(input("Please enter the temperature:"))
   kind = input("Please enter 'C' for Celsius, or 'K' for Kelvin:")
   if(temp <= 0 and kind == "C"):
       print("At this temperature, water is solid.")
   if(0 < temp < 100 and kind == "C"):
       print("At this temperature, water is a liquid.")
   if(temp >= 100 and kind == "C"):
       print("At this temperature, water is a gas.")
   if(temp <= 273.15 and kind == "K"):
       print("At this temperature, water is a solid.")
   if(273.15 < temp < 373.15 and kind == "K"):
       print("At this temperature, water is a liquid.")
   if(temp >= 373.15 and kind =="K"):
       print("At this temperature, water is a gas.")
main()
