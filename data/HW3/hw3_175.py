def main():
    temperature = float(input("Please enter the temperature: "))
    tempScale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if (temperature <= 0 and tempScale == "C") or (temperature <= 273.15 and tempScale == "K"):
        print("At this temperature, water is a (frozen) solid.")
    elif(temperature >= 100 and tempScale == "C") or (temperature >= 373.15 and tempScale == "K"):
        print("At this temperature, water is a gas.")
    elif tempScale == "C" or tempScale == "K":
        print("At this temperature, water is a liquid.")
    else:
        print("One of your inputs was incorrect. Please try again.")
main() 
