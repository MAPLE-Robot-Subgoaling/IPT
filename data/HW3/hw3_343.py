def main():
    temperature = float(input("Please enter the temperature: "))
    tempUnit = input("Please enter 'C' for Celsius, or 'K' for Kevin: ")
    waterState = "No State"
    if tempUnit == "K":
        temperature = temperature - 273.15
    if temperature < 0:
        waterState = "solid."
    elif temperature < 100:
        waterState = "liquid."
    else:
        waterState = "gas."
    print("At this temperature, water is a", waterState)
    print("")
main()
