def main():
    CELSIUS = "C"
    KELVIN = "K"
    SOLID_C = 0.0
    GAS_C = 100.0
    SOLID_K = 273.16
    GAS_K = 373.16
    userTemperature = float(input("Enter the temperature: "))
    userScale = input("Enter 'C' if it is in Celsius, 'K' if it is in Kelvin: ")
    if userScale == CELSIUS:
        if userTemperature >= GAS_C:
            print("At this temperature, water is a gas.")
        if userTemperature <= SOLID_C: 
            print("At this temperature, water is a solid.")
        if (userTemperature > SOLID_C) and (userTemperature < GAS_C):
            print("At this temperature, water is a liquid.")
    if userScale == KELVIN:
        if userTemperature >= GAS_K:
            print("At this temperature, water is a gas.")
        if userTemperature <= SOLID_K:
            print("At this temperature, water is a solid.")
        if (userTemperature > SOLID_K) and (userTemperature < GAS_K):
            print("At this temperature, water is a liquid.")
main()
