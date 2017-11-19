def main():
    temperature = float(input("Please input the temperature:"))
    C = 0
    K = 0
    measured = input("Please enter a 'C' for Celsius or 'K' for Kelvin")
    if measured == "C":
        if temperature <= 0:
            print("The water is a solid")
        elif temperature > 0 and temperature < 100:
            print("The water is a liquid")
        elif temperature >= 100:
            print("The water is a gas")
    elif measured == "K":
        if temperature <= -273.15:
            print("The water is a solid")
        elif temperature > -273.15 and temperature < 273.15:
            print(" The water is a liquid")
        elif temperature >= 273.15:
            print("The water is a gas")
main()
