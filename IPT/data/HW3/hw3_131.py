
def main():

    temperature = float(input("Please enter the temperature: "));
    unit = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: "));
    
    if (unit == "K"):
        if (temperature < 273.16):
            print("At this temperature, water is a solid. ");
        elif(temperature > 373.16):
            print("At this temperature, water is a gas. ");
        else:
            print("At this temperature, water is a liquid. ");

    elif (unit == "C"):
        if (temperature < 0):
            print("At this temperature, water is a solid. ");
        elif (temperature > 100):
            print("At this temperature, water is a gas. ");
        else:
            print("At this temperature, water is a liquid. ");

main()
