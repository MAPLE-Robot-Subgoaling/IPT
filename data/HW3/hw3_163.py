def main():
    FREEZING_POINT_K = 273.15
    FREEZING_POINT_C = 0
    BOILING_POINT_K = 373.15
    BOILING_POINT_C = 100
    temperature = float(input("Please enter the temperature:"))
    temp_type = input("Please enter 'C' for Celsius, or 'K' for kelvin:")
    if temp_type == "C":
        if temperature > FREEZING_POINT_C and temperature < BOILING_POINT_C:
            print("Water is a liquid at this temperature.")
        elif temperature <= FREEZING_POINT_C:
            print("Water is a solid at this temperature.")
        else:
            print("Water is a gas at this temperature.")
    elif temp_type == "K":
        if temperature > FREEZING_POINT_K and temperature < BOILING_POINT_K:
            print("Water is a liquid at this temperature.")
        elif temperature <= FREEZING_POINT_K:
            print("Water is a solid at this temperature.")
        else:
            print("Water is a gas at this temerature.")
main()
