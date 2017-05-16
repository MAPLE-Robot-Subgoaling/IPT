
def main():
    
    tempNum = float(input("Please enter the temperature: "))
    type = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    conclusions = ["At this temperature, water is a gas","At this temperature, water is a liquid","At this temperature, water is a solid"]
    conclusion = ""
    if(type == "C"):
        if(tempNum >= 100):
            conclusion = conclusions[0]
        elif(tempNum < 100 and tempNum > 0):
            conclusion = conclusions[1]
        else:
            conclusion = conclusions[2]
    elif(type == "K"):
        if(tempNum >= 373.16):
            conclusion = conclusions[0]
        elif(tempNum < 373.16 and tempNum > 273.16):
            conclusion = conclusions[1]
        else:
            conclusion = conclusions[2]
    else:
        print("Invalid type")
    print(conclusion)
main()
