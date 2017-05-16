
def main():
    KELVIN_CONSTANT = float(273.15)

    scale = input("Input a temperature scale ('c' for celsius, 'k' for kelvin) ")
    temp = float(input("What temperature are you interested in? "))

    if scale == "k":
        temp = temp - KELVIN_CONSTANT

    if temp >= 100:
        print("Water is a gas at this temperature.")
    if temp <= 0:
        print("Water is a solid at this temperature.")
    if temp < 100 and temp > 0:
        print("Water is a liquid at this temperature.")    
main()
