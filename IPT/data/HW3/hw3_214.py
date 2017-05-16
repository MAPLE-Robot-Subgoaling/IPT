
def main():
 temp = float(input("Hello. Please enter the temperature:",))
 form  =str( input("Thanks. Now enter 'C' for Celsius form, or 'K' for Kelvin form:",))
 if form == "C":
  if temp >= 100:
   print("For the current temperature, water is in a gas form.")
  elif temp <= 0:
   print("For the current temperature, water is in a solid form.")
  else:
   print("For the current temperature, water is in a liquid form.")
 else:
  if temp >= 373.16:
   print("For the current temperature, water is in a gas form.")
  elif temp <= 273.16:
   print("For the current temperature, water is in a solid form.")
  else:
   print("For the current temperature, water is in a liquid form.")
main()
