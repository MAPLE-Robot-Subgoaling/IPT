
def main():


    WATER_SOLID_CELSIUS = 0

    WATER_LIQUID_CELSIUS = 100

    WATER_SOLID_KELVIN = 273

    WATER_LIQUID_KELVIN = 373


    temperature = float(input("Please enter the temperature: "))

    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")


    if scale == 'C':

        if temperature <= WATER_SOLID_CELSIUS:

            print("At this temperature, water is a solid.")

        elif temperature > WATER_SOLID_CELSIUS and temperature <= WATER_LIQUID_CELSIUS:

            print("At this temperature, water is a liquid.")

        elif temperature > WATER_LIQUID_CELSIUS:

            print("At this temperature, water is a gas.")

    elif scale == 'K':

        if temperature <= WATER_SOLID_KELVIN:

            print("At this temperature, water is a solid.")

        elif temperature > WATER_SOLID_KELVIN and temperature <= WATER_LIQUID_KELVIN:

            print("At this temperature, water is a liquid.")

        elif temperature > WATER_LIQUID_KELVIN:

            print("At this temperature, water is a gas.")




main()

