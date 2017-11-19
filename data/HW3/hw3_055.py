def main():
    temp = float(input("Please enter the temperature: "))
    kind = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if(kind == 'C'):
       if(temp < 0):
          print("At this temperature, water is a solid!")
       if( temp <= 100 and temp >= 0):
          print("At this temperature, water is a liquid!")
       if(temp > 100):
          print("At this temperature, water is a Gas!")
    else:
        if(temp < 273):
            print("At this temperature, water is a Solid!")
        if(temp <= 373 and temp >= 273):
            print("At this temperature, water is a Liquid!")
        if(temp > 373):
            print("At this temperature, water is a Gas!")
main()
