
def waterState():
   temp = int(input("Please enter the temperature: "));
   unit = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ");
   if (unit == "K"):
      temp = (temp - 273);
   else:
      temp = temp;
   if (temp < 0):
      print("At this temperature, water is solid.");
   elif (temp < 100):
      print("At this temperature, water is liquid.");
   else:
      print("At this temperature, water is a gas.")
   return




waterState()
