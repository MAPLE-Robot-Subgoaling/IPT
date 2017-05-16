def main():
    temperature = float(input("Please enter the temperature:"))
    tempScale = input("Please enter 'C' for Celsius, or 'K' for Kelvin")
    if(tempScale == 'C'):
        if(temperature <= 0.0):
            print("At ",temperature,"degrees Celsius, water is a solid")
        elif(temperature >=100.0):
            print("At ",temperature,"degrees Celsius, water is a gas")
        else:
            print("At ",temperature,"degrees Celsius, water is a liquid")
    elif(tempScale == 'K'):
        if(temperature <=273.15):
            print("At ",temperature,"degrees Kelvin, water is a solid")
        elif(temperature >= 373.15):
            print("At ",temperature,"degrees Kelvin, water is a gas")
        else:
            print("At ",temperature,"degrees Kelvin, water is a liquid")
    else:
        print("Unknown temperature scale")       

main()
