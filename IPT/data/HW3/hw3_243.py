
def main():
   temp =float(input("please enter a temperature "))
   unit = input("please enter 'C' for celsius or 'K' for kelvin ")
   if unit=="C":
      if temp <0:
          print("At this temperature, water is a solid")
      elif temp >100:
          print("At this temperature, water is a gas")
      elif temp >0 and temp <100:
          print("At this temperature, water is a liquid")
   elif unit=="K":
      if temp <273.16:
          print("At this temperature, water is a solid")
      elif temp >373.16:
          print("At this temperature, water is a gas")
      elif temp >273.16 and temp <373.16:
          print("At this temperature, water is a liquid")
main()

