def main():
    temp = float(input("Please enter a temperature"))
    degree = input("Please enter 'C' for Celsius or 'K' for Kelvin")
    if( degree == "C"):
           if(temp <= 0):
                     print("At this temp, water is a solid")
           elif(temp >= 100):
                     print("At thie temp, water is a gas")
           else:
                     print("At this temp, water is a liquid")
    if( degree == "K"):
           if( temp <= 273.15):
                     print("At this temp, water is a solid")
           elif( temp >= 100):
                     print("At this temp, water is a gas")
           else:
                     print("At this temp, water is a liquid")
main()
