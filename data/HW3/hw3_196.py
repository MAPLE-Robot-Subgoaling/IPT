def main():
    user_temp = float(input("Please enter the temperature: "))
    user_scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if user_scale == 'K': 
         if user_temp < 273.15:
             print("At this temperature, water is a (frozen) solid.")
         elif user_temp > 373.15:
             print("At this temperature, water is a gas.")
         else:
             print("At this temperature, water is a liquid.")
    if user_scale == 'C':
         if user_temp < 0:
             print("At this temperature, water is a (frozen) solid.")
         elif user_temp > 100:
             print("At this temperature, water is a gas.")
         else:
             print("At this temperature, water is a liquid.")
main()
