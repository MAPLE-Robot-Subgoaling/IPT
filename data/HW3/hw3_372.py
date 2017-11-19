SOLID_CEL = 0
SOLID_KEL = 273.16
GAS_CEL = 100
GAS_KEL = 373.16
def main():
    temp = float(input("Please enter the temperature: "))
    tempScale = input("Please enter 'c' for Celcius, or 'k' for Kelvin: ")
    if(tempScale == 'c'):
        if(temp <= SOLID_CEL):
             print("At this temperature, water is a (frozen) solid.")
        elif(temp >= GAS_CEL):
             print("At this temperature, water is a gas.")
        elif((temp > SOLID_CEL) and (temp < GAS_CEL)):
             print("At this temperature, water is a liquid.")
    if(tempScale == 'k'):
         if(temp <= SOLID_KEL):
             print("At this temperature, water is a (frozen) solid.")
         elif(temp >= GAS_KEL):
             print("At this temperature, water is a gas.")
         elif((temp > SOLID_KEL) and (temp < GAS_KEL)):
             print("At this temperature, water is a liquid.")
main()
