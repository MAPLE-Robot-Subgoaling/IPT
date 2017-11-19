def main():
    temp = float(input("Please enter in the temperature: "))
    unit = input("Please enter C for Celsius and K for Kelvin: ")
    if (unit ==" C"):
      degreeK  = temp + 273.15
      if (degreK >= 373): 
         print("At this temperature, water is a gas")
      if (degreeK <= 273): 
         print("At this temperature, water is a solid")
      if (degreeK > 274 and degreeK < 373):
         print("At this temperature, water is a liquid")
    else: 
      if (temp >= 373):
         print("At this temperature, water is at gas")
      if (temp <= 273):
         print ("At this temperature, water is a solid")
      if (temp > 274 and temp < 373):
         print("At this temperature water ia a liquid")
main() 
