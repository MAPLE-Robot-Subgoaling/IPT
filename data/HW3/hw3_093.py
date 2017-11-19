def main():
    Temperature = int(input("please enter the temperature: "))
    tempSystem = input("Please enter 'C' for celsius or 'K' for kelvin")
    if Temperature >= 100 and tempSystem == "C":
        print("water is gas at this temperature")
    elif Temperature >= 373 and tempSystem == "K":
        print("water is gas at this temperature")
    elif Temperature <= 0 and tempSystem == "C":
        print("water is solid at this temperature")
    elif Temperature <= 273 and tempSystem == "K":
        print("water is solid at this temperature")
    else:
        print("water is liquid at this temperature")
main()
