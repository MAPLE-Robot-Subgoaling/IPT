
def main():

    temperature = float(input("Please enter the temperature: "))
    type_of_temp = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    
    if type_of_temp =="C" and temperature<32:
        print("At this temperature, water is a (frozen) solid")
    
    if type_of_temp=="C" and temperature >= 32 and temperature<100:
        print("At this temperature, water is a liquid")

    if type_of_temp=="C" and temperature >= 100:
        print("At this temperature, water becomes a gas")

    if type_of_temp == "K" and temperature <273:
        print("At this temperature, water is a (frozen) solid")

    if type_of_temp == "K" and temperature >=273 and temperature <373.2:
        print("At this temperature, water is a liquid")

    if type_of_temp == "K" and temperature>=373.2:
        print("At this temperature, water becomes a gas")


main()
