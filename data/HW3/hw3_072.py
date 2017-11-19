def main():
    GAS_K = 373.16
    SOLID_K = 273.16
    GAS_C = 100
    SOLID_C = 0
    temp = float(input("Please enter the temperature: "))
    scale = input("Please enter a 'C' for Celsius and a 'K' for Kelvin: ")
    if scale == "K" and temp >= GAS_K:
        print("At this temperature, water is a gas.")
    if scale == "K" and temp <= SOLID_K:
        print("At this temperature, water is a solid.")
    if scale == "K" and temp < GAS_K and temp > SOLID_K:
        print("At this temperature, water is a liquid.")
    if scale == "C" and temp >= GAS_C:
        print("At this temperature, water is a gas.")
    if scale == "C" and temp <= SOLID_C:
        print("At this temperature, water is a solid.")
    if scale == "C" and temp < GAS_C and temp > SOLID_C: 
        print("At this temperature, water is a liquid.")
main()
