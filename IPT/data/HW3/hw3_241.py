
def main():
    temp = float(input("Please enter the temperature: "))
    unit = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: "))

    Kelv = 273.0

    if unit == "K":
        temp = temp - Kelv

    if temp >= 100:
        print("At this temperature, water is a gas")
    elif temp <= 0:
        print("At this temperature, water is a solid")
    else:
        print("At this temperature, water is a liquid")

main()
