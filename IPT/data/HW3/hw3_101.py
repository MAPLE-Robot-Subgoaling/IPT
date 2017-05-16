
def main():
    waterTemp = float(input("Please enter the temperature: "))
    tempState = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if tempState == "C" and waterTemp < 0: 
        print ("At this temperature, water is a (frozen) solid")
    if waterTemp >= 0 and waterTemp <= 100 and tempState == "C":
        print ("At this temperature, water is a liquid")
    if waterTemp > 100 and tempState == "C":
        print ("At this temperature, water is a gas")
    
    if tempState == "K" and waterTemp < 32:
        print ("At this temperature, water is a (frozen) solid")
    if waterTemp >= 32 and waterTemp <= 212 and tempState == "K":
        print ("At this temperature, water is a liquid")
    if waterTemp > 212 and tempState == "K":
        print ("At this temperature, water is a gas")
main()
