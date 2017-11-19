CELCIUS_FROZEN = 0
CELCIUS_BOILING = 100
KELVIN_FROZEN = 273
KELVIN_BOILING = 373
def main():
    temp = float(input("Please enter the temperature: "))
    scale = str(input("Enter 'C' for Celsius or 'K' for Kelvin: "))
    if scale == "C":
        if temp <= CELCIUS_FROZEN:
            print("Water is a solid at this temperature.")
        elif temp >= CELCIUS_BOILING:
            print("Water is a gas at this temperature.")
        else:
            print("Water is a liquid at this temperature.")
    elif scale == "K":
        if temp <= KELVIN_FROZEN:
            print("Water is a solid at this temperature.")
        elif temp >= KELVIN_BOILING:
            print("Water is a gas at this temperature.")
        else:
            print("Water is a liquid at this temperature.")
main()
