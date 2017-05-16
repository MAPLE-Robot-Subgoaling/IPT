

def main():

    temperature = float(input("Please enter the temperature: "))

    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")

    if(scale == 'C'):
        if(temperature <= 0):
            print("At this temperature, water is a (frozen) solid.")
        elif(0 < temperature < 100):
            print("At this temperature, water is a liquid.")
        elif(temperature >= 100):
            print("At this temperature, water is a gas.")

    elif(scale == 'K'):
        if(temperature <= 273.15 ):
            print("At this temperature, water is a (frozen) solid.")
        elif(273.15 < temperature < 373.15 ):
            print("At this temperature, water is a liquid.")
        elif(temperature >= 373.15):
            print("At this temperature, water is a gas.")
    
main()
