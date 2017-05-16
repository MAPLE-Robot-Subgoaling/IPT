
def main():
    response = float( input("Please enter the temperature: "))
    response_2 = input("Please enter 'C' for Celcius, or 'K' for Kelvin: ")
    if response_2 == "C":
        if response <= 0:
            print("At this temperature, water is a solid")
        elif response >= 100:
            print("At this temperature, water is a gas")
        else:
            print("At this temperature, water is  a liquid")
    else:
        if response <= 0:
            print("At this temperature, water is a solid")
        elif response >= 373.16:
            print("At this temperature, water is  a gas")
        else:
            print("At this temperature, water is a liquid")
main()
