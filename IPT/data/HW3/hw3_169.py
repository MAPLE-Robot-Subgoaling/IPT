
def main():
    waterTemp = float(input('Please enter the temperature: '))
    unit = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if unit == 'C' and waterTemp <= 0:
        print('At this temperature, the water is a (frozen) solid.')
    elif unit == 'C' and waterTemp > 0 and waterTemp < 100:
        print('At this temperature, the water is a liquid.')
    elif unit == 'C' and waterTemp >= 100:
        print('At this temperature, the water is a gas.')
    elif unit == 'K' and waterTemp <= 273.15:
        print('At this temperature, the water is a (frozen) solid.')
    elif unit == 'K' and waterTemp > 273.15 and waterTemp < 373.15:
        print('At this temperature, the water is a liquid.')
    elif unit == 'K' and waterTemp >= 373.15:
        print('At this temperature, the water is a gas.')

main()



