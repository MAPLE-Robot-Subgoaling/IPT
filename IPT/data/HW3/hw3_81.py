
def main():
 
    Temp = float(input("What is the current temperature?"))
    Unit = (input("Is the temperature in 'C' for Celsius, or 'F' for Fahrenheit?"))
    if (Temp >= 100 and Unit == 'C'):
        print("At this temperature, water is a gas.")
    if (Temp >= 132 and Unit == 'F'):
        print("At this temperature, water is a gas.")
    if (Temp < 0 and Unit == 'C'):
        print("At this temperature, water is frozen")  
    if (Temp < 32 and Unit == 'F'):
        print("At this temperature, water is frozen")
    if (Temp > 0 and Temp < 100 and Unit == 'C'):
        print("At this temperatire, water is a liquid")
    if (Temp > 32 and Temp < 132 and Unit == 'F'):
        print("At this temperatire, water is a liquid")

main()
