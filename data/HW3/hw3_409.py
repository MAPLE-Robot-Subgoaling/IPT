def main():
    temperature = float(input("What is the temperature? "))
    scale = input("What is the scale the temperature is measured in? ")
    if temperature >= 100 and scale == "C":
        print("At this temperature, water is a gas.")
    elif temperature > 0 and scale == "C":
        print("At this temperature, water is a liquid")
    elif temperature < 0 and scale == "C":
        print("At this temperature, water is a solid")
    elif temperature >= 373 and scale == "K":
        print("At this temperature, water is a gas")
    elif temperature > 273 and scale == "K":
        print("At this temperature, water is a liquid")
    elif temperature < 273 and scale == "K":
        print("At this temperature, water is a solid")
main()
