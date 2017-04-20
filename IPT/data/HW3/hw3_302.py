
def main():

    water_sC= 0
    water_gC= 100
    water_sK= 273.16
    water_gK= 373.16
    num1= float(input("Please enter the temperature: "))
    unit= input("Please enter 'C' or Celcius, or 'K' for Kelvin: ")
    if unit == "K" and num1 < water_sK:
        print("At this temperature, water is a (frozen) solid.")
    elif unit == "K" and num1 > water_gK:
        print("At this temperature, water is a gas.")
    elif unit == "K" and num1 > water_sK and num1 < water_gK:
        print("At this temperature, water is a liquid.")
    elif unit == "C" and num1 < water_sC:
        print("At this temperature, water is a (frozen) solid.")
    elif unit == "C" and num1 > water_gC:
        print("At this temperature, water is a gas.")
    elif unit == "C" and num1 > water_sC and num1 < water_gC:
        print("At this temperature, water is a liquid.")
main()
