
def main():
    
    print()
    temp = float(input("Please enter the Temperature: ")) #casts input to float
    temptype = input("Please enter an uppercase 'C' for Celsius or uppercase 'K' for Kelvin: ")

    if temptype == "C":
        if temp >= 100: #Computes the if statement that 'temp' validates
            print("At this temperature, water is a Gas")
        elif temp <= 0:
            print("At this temperature, water is (frozen) Solid")
        else:
            print("At this temperature, water is a Liquid")
           
    elif temptype == "K":
        if temp >= 373.15: #Computes the if statement that 'temp' validates             
            print("At this temperature, water is a Gas")
        elif temp <= 273.15:
            print("At this temperature, water is (frozen) Solid")
        else:
            print("At this temperature, water is a Liquid")
    print()

main()
