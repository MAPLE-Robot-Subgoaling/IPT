
def main():

    inputTemp=float(input("Please enter the temperature: "))
    inputUnit=str(input("Please enter 'C' for Celcius or 'K' for Kelvin: "))
   
    if inputUnit == 'K':
        realTemp=(inputTemp-273)*(9/5)+32
    else:
        realTemp=inputTemp*(9/5)+32

    if realTemp >= 212:
        print("At this temperature, water is a gas.")
    elif realTemp >= 32:
        print("At this temperature, water is a liquid.")
    else:
        print("At this temperature, water is a (frozen) solid.")

main()
