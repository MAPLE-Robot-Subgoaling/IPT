
def main():

    temp = float(input("What is the temperature? "))
    unit = input("Is the temperature in Celcius 'C' or Kelvin 'K'? ")
    if (unit == "C"):
         if (temp > 100):
              print("Water is a gas at", temp,"degrees C")
         elif (temp < 0):
              print("Water is a solid at", temp,"degrees C")
         else:
              print("Water is a liquid at", temp,"degrees C")
    if (unit == "K"):
         if (temp > 373.15):
              print("Water is a gas at", temp,"K")
         elif (temp < 273.15):
              print("Water is a solid at", temp,"K")
         else:
              print("Water is a liquid at", temp,"K")

main()
