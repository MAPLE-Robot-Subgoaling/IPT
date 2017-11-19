def main():
    temp = float(input("Please enter the temperature:"))
    tempUnit = input("Please enter 'C' for Celsius, or 'K' for Kelvin:")
    if (temp <= float("32")) and (tempUnit == "C"):
        print("At this temperature, water is a (frozen) solid.")
    if (temp >= float("100")) and (tempUnit == "C"):
        print("At this temperature, water is a gas.")
    if (temp >= float("32")) and (temp <= float("100")) and (tempUnit == "C"):
        print("At this tempurature, water is a liquid.")
    if (tempUnit == "K") and (temp <= float("273.16")):
        print("At this temperature, water is a (froxen) solid.")
    if (tempUnit == "K") and (temp >= float("373.16")):
        print("At this temperature, water is a gas.")
    if (tempUnit == "K") and (temp >= float("273.16")) and (temp <=float("373.16")):
        print("At this temperature, water is a liquid.")
main()
