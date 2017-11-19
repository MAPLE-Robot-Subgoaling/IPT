def main():
    freezingPointinC = 0
    boilingPointinC = 100
    freezingPointinK = 273.15
    boilingPointinK = 373.15
    temperature = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if scale == "C":
        if temperature <= freezingPointinC:
            print("At this temperature, water is a (frozen) solid.")
        elif freezingPointinC < temperature < boilingPointinC:
            print("At this temperature, water is a liquid.")
        elif temperature >= boilingPointinC:
            print("At this temperature, water is a gas.")
    elif scale == "K":
        if temperature <= freezingPointinK:
            print("At this temperature, water is a (frozen) solid.")
        elif freezingPointinK < temperature < boilingPointinK:
            print("At this temperature, water is a liquid.")
        elif temperature >= boilingPointinK:
            print("At this temperature, water is a gas.")
main()
