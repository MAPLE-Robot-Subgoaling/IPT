
def main():
    
    temperature = float(input("Please enter the temperature: "))
    mode = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    state = ""

    if (mode == "C"):
        if (temperature <= 0):
            state = "solid"
        elif (temperature >= 100):
            state = "gas"
        else:
            state = "liquid"
    elif (mode == "K"):
        if (temperature <= 273.15):
            state = "solid"
        elif (temperature >= 373.15):
            state = "gas"
        else:
            state = "liquid"
        
    print ("At this temperature, water is a", state)

        
main()
