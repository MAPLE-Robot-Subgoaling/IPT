
def main():

    temp = float(input("What is the temperature? "))
    print ("Please answer with either an C or K")
    Kelvin_Celsius = input("Is your temperature in Celsius or Kelvin? ")
    if Kelvin_Celsius == "C" and temp >= 100:
        print ("At",temp,"degrees",Kelvin_Celsius,"your water is a gas")
    if Kelvin_Celsius == "C" and temp < 100 and temp > 0:
        print ("At",temp,"degrees",Kelvin_Celsius,"your water is a liquid")
    if Kelvin_Celsius == "C" and temp < 0:
        print ("At",temp,"degrees",Kelvin_Celsius,"your water is a solid")
    if Kelvin_Celsius == "K" and temp >= 373.2:
        print ("At",temp,"degrees",Kelvin_Celsius,"your water is a gas")
    if Kelvin_Celsius == "K" and temp < 373.2 and temp > 273.2:
        print ("At",temp,"degrees",Kelvin_Celsius,"your water is a liquid")
    if Kelvin_Celsius == "K" and temp < 273.2:
        print ("At",temp,"degrees",Kelvin_Celsius,"your water is a solid")
main()
