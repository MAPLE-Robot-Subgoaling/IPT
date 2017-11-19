temp = float(input("Please enter the temperature: "))
scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
MELTING_POINT_C = 32
BOILING_POINT_C = 100
MELTING_POINT_K = 273.15
BOILING_POINT_K = 373.15
def main():
             if scale == "C":
                 if temp >= 0 and temp < MELTING_POINT_C:
                     print("At this temperature, water is a (frozen) solid.")
                 elif temp >= MELTING_POINT_C and temp < BOILING_POINT_C:
                     print("At this temperature, water is a liquid.")
                 elif temp >= BOILING_POINT_C:
                     print("At this temperature, water is a gas.")
             else:
                 if temp >= 0 and temp < MELTING_POINT_K:
                     print("At this temperature, water is a (frozen) solid.")
                 elif temp >= MELTING_POINT_K and temp < BOILING_POINT_K:
                     print("At this temperature, water is a liquid.")
                 elif temp >= BOILING_POINT_K:
                     print("At this temperature, water is a gas.")
main()
