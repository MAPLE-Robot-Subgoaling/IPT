

def main():

    temp = float(input("Please enter the temperature: "))
    scale = str(input("Please eneter C for Celsius, or K for Kelvin: "))
    frozen = "At this temperature, water is a (frozen) solid."
    liquid = "At this temperature, water is a liquid."
    gas = "At this temperature, water is a gas"

    if(scale == "C"):
        if(temp <= 0):
            print(frozen)
        if(temp > 0 and temp <= 100):
            print(liquid)
        if(temp > 100):
            print(gas)
    if(scale == "K"):
        if(temp <= 273.15):
            print(frozen)
        if(temp > 273.15 and temp < 373.15):
            print(liquid)
        if(temp > 373.15):
            print(gas)
main()
