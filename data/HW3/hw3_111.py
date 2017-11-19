def main():
       scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin:")
       temp = float(input("Please enter the temperature:"))
       if scale == "K" or scale == "k" :
         if temp >= 273.15 and temp < 373.15:
           print(" At this temperature, water is a liquid")
         elif temp < 273.15:
           print(" At this temperature, water is a (frozen) solid.")
         else :
           print("At this temperature, water is a gas.")
       if scale == "C" or scale == "c" : 
         if temp >= 0 and temp < 100:
           print(" At this temperature, water is a liquid")
         elif temp <= 0:
           print(" At this temperature, water is a (frozen) solid.")
         else :
           print("At this temperature, water is a gas.")
main()
