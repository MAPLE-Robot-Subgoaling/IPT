def main():
    temperature = "0"
    tempScale = "C"
    print("Hello and welcome to the water state wizard!")
    temperature = float(input("Please enter the temperature: "))
    tempScale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if tempScale == "C":
        if temperature <= 0:
            print("At this temperature, water is a solid.")
        elif temperature <= 100:
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a gas.")
    else:
        if temperature <= 273.16:
            print("At this temperature, water is a solid.")
        elif temperature <= 373.16:
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a gas.")
    print("Thank you for using our water state wizard!")
main()
