
def main():
    CELSIUS = 'C'
    KELVIN = 'K'
    num = float(input("Please enter the temperature: "))
    temp = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if temp == CELSIUS:
        if num <= 0:
            print("At this temperature, the water is solid")
        elif num > 0 and num < 100:
            print("At this temperature, the water is liquid")
        elif num >= 100:
            print("At this temperature, the water is a gas")
    elif temp == KELVIN:
        if num <= 273.16:
            print("At this temperature, the water is solid")
        elif num > 273.16 and num < 373.16:
            print("At this temperature, the water is liquid")
        elif num >= 373.16:
            print("At this temperature, the water is a gas")
main()
