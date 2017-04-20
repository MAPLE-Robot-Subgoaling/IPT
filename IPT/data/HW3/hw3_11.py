def main():
    temperature = (float)(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin ")

    if(scale == "C"):
        if(temperature >= 100):
            print("At this temperature, the water is gas")
        elif(temperature <= 0):
            print("At this temperature, the water is solid")
        else:
            print("At this temperature, the water is liquid")
    else: #Scale is Kelvin
        if(temperature >= 373.15):
            print("At this temperature, the water is gas")
        elif(temperature <= 273.15):
            print("At this temperature, the water is solid")
        else:
            print("At this temperature, the water is liquid")
main()
