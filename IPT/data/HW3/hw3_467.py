def main():
    inputTemperture = float(input("Please enter the temperture: "))
    typeTemperture = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    
    if typeTemperture == "C":
        boilingTemp = 100.0
        freezingTemp = 0.0
        absoluteZero = -273.0
        print("You are using Celius")
        if inputTemperture >= boilingTemp:
            print("At this temperture, water is a gas")
        if boilingTemp > inputTemperture > freezingTemp:
            print("At this temperture, water is a liquid")
        if freezingTemp >= inputTemperture > absoluteZero:
            print("At this temperture, water is a (frozen) soild")
        if absoluteZero >= inputTemperture:
            print("At this temperture, water is at absolute zero")
    
    if typeTemperture == "K":
        print("You are using Kelvin")
        boilingTemp = 373.0 
        freezingTemp = 273.0
        absoluteZero = 0.0
        if inputTemperture >= boilingTemp:
            print("At this temperture, water is a gas")
        if boilingTemp > inputTemperture > freezingTemp:
            print("At this temperture, water is a liquid")
        if freezingTemp >= inputTemperture > absoluteZero:
            print("At this temperture, water is a (frozen) soild")
        if absoluteZero >= inputTemperture:
            print("At this temperture, water is at absolute zero")
main()
