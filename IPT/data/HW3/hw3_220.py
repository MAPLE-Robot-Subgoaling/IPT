
def main():
    temperature = (float)(input('Please enter the temperature:'))
    scale = input('Please enter \'C\' for Celsius, or \'K\' for Kelvin')
    if scale == "K": #converting Kelvin into Celsius to make this easier lol
        temperature = temperature - 273
    if temperature > 100:
        print("Water is a gas at this temperature.")
    elif temperature < 32:
        print("Water is a solid at this temperature.")
    else:
        print("Water is a liquid at this temperature.")
main()