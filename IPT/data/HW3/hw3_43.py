
def main():

    temp = float(input("Enter the temperature: "))
    scale = input("Enter 'C' for Celsius and 'K' for Kelvin: ")
    
    if (scale == "K"):
        cTemp = temp + 273.15
    if (scale == "C"):
        cTemp = temp
    if (cTemp <= 0):
        print("At this temperature, water is a (frozen) solid")
    elif (cTemp < 100):
        print("At this temperature, water is a liquid")
    elif (cTemp >= 100):
        print ("At this temperature, water is a gas")

main()
