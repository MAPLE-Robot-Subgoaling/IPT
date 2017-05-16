
def main():

   temp = float(input("Please enter the temperature: "))
   temptype = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: "))

   if temptype == "K":
      if temp >= 373.16:
         print("Water is a gas at this temperature.")
      if temp < 373.16 and temp > 273.16:
         print("Water is a liquid at this temperature.")
      if temp <= 273.16:
         print("Water is solid at this temperature.")
   if temptype == "C":
      if temp >= 100:
         print("Water is a gas at this temperature.")
      if temp < 100 and temp > 0:
         print("Water is a liquid at this temperature.")
      if temp <= 0:
         print("Water is a solid at this temperature.")
main()
