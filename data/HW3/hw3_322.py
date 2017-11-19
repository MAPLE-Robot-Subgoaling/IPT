def main():
 temprature = float(input("Please enter the temprature: "))
 tempChoice = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
 if tempChoice == "C": 
  if temprature <= 32:
   print("At this temprature, water is (frozen) solid")
  if 32 < temprature < 100:
   print("At this temprature, water is liquid")
  if temprature > 100:
   print("At this temprature, water is gas")
 if temprature == "K":
  if temprature < 273.16:
   print("At this temprature, water is (frozen) solid")
  if 273.16 < temprature < 373.16:
   print("At this temprature, water is a liquid")
  if temprature > 373.16:
   print("At this temprature, water is a gas")
main()
