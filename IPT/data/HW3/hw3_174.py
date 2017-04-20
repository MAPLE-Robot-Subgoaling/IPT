def main():
    temp = int(input("Please enter the temperature: "))
    tempType = input("Please enter 'C' if celsius or 'K' if kelvin: ")
    if(tempType == 'C'):
        if(temp<=0):
            print("At this temperature, water is solid")
        elif(temp>0 and temp<100):
            print("At this temperature, water is liquid")
        elif(temp>=100):
            print("At this temperature, water is gas")
    elif(tempType == 'K'):
         if(temp<=273.15):
            print("At this temperature, water is solid")
         elif(temp>273.15 and temp<373.15):
            print("At this temperature, water is liquid")
         elif(temp>=373.15):
            print("At this temperature, water is gas")

    else:
        print("Celsius or Kelvin not specified")

main()
