

def main():

    CELSIUS_FROZEN = 0
    CELSIUS_GAS = 100
    KELVIN_FROZEN = 273
    KELVIN_GAS = 373

    temp = float(input("Please enter the temprature: "))
    scale = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: "))
    
    if scale == "C":

        if temp >= CELSIUS_GAS:
            print(" At this temperature, water is a gas.")
        if temp <= CELSIUS_FROZEN:
            print(" At this temperature, water is a (forzen) solid.")
        if temp < CELSIUS_GAS and temp >  CELSIUS_FROZEN:
            print(" At this temperature, water is a liquid.")
    if scale == "K":
        
        if temp >= KELVIN_GAS:
            print(" At this temperature, water is a gas.")
        if temp <= KELVIN_FROZEN:
            print(" At this temperature, water is a (forzen) solid.")
        if temp < KELVIN_GAS and temp > KELVIN_FROZEN:
            print(" At this temperature, water is a liquid.")
main()




    
