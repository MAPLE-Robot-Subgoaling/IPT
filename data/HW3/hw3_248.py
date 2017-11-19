def main():
    temp = float(input("Please enter the temperature: ")) 
    units = input("Please enter 'C' for Celcius or 'K' for Kelvin : ")
    if units == "C":
        if temp <= 0:
            state = "solid"
        elif temp < 100:
            state = "liquid"
        else:
            state = "gas"
    else:
        if temp <= 273.2:
            state = "solid"
        elif temp < 373.2:
            state = "liquid"
        else:
            state = "gas"
    print("At this temperature, water is a "+state+".")
main() 
