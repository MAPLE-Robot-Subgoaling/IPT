

def main():

    userNum = float(input("Please enter the temperature: "))
    userTemp = input("Please enter 'C' for Celsius and 'K' for Kelvin: ")

    if userTemp == 'C':
        if userNum > 0 and userNum < 100:
            print("At this temperature, water is a liquid.")
        elif userNum < 0:
            print("At this temperature, water is (frozen) solid.")
        else:
            print("At this temperature, water is a gas.")
        
    if userTemp == 'K':
        if userNum > 273.15 and userNum < 373.15:
            print("At this temperature, water is a liquid.")
        elif userNum < 273.15:
            print("At this temperature, wate is (frozen) solid")
        else:
            print("At this temperature, water is a gas")
main()
