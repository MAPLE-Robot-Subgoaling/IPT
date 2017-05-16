
def main():
    temp = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if(scale == "K"):
        if(temp < 0):
            print("At this temperature, water is below absolute zero.")
        if(temp == 0):
            print("At this temperature, water is absolute zero.")
        if(temp > 0 and temp < 273):
            print("At this temperature, water is beginning to freeze.")
        if(temp == 273):
            print("At this temperature, water is a (frozen) solid.")
        if(temp > 273 and temp < 373):
            print("At this temperature, water is beginning to boil.")
        if(temp == 373):
            print("At this temperature, water is boiling.")
        if(temp > 373):
            print("At this temperature, water is a gas, or beyond.")
    if(scale == "C"):
        if(temp < -273):
            print("At this temperature, water is below absolute zero,")
        if(temp == -273):
            print("At this temperature, water is absolute zero.")
        if(temp < 0 and temp > -273):
            print("At this temperature, water is beginning to freeze.")
        if(temp == 0):
            print("At this temperature, water is a(frozen) solid.")
        if(temp > 0 and temp < 100):
            print("At this temperature, water is beginning to boil.")
        if(temp == 100):
            print("At this temperature, water is boiling.")
        if(temp > 100):
            print("At this temperature, water is a gas, or beyond.")
main()
