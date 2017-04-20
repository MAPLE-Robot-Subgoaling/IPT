
def main():

    var_temp = float(input("Please enter the temperature: "))
    var_type = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: "))

    if var_type == "C":
        if var_temp <= 0:
            print("At this temperature, water is a (frozen) solid.")
        elif var_temp >= 100:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")

    else:
        if var_temp <= 32:
            print("At this temperature, water is a (frozen) solid.")
        elif var_temp >= 212:
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")

main()
