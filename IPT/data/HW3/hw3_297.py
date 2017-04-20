
def main():
    temp = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if (scale == "K"):
        temp-=273.15
    if(temp<=0):
        print("At this temperature, water is solid")
    elif(temp<=100):
        print("At this temperature, water is liquid")
    else:
        print("At this temperature, water is a gas")
main()
