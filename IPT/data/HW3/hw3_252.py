
def main():
    
    degree = input("Please enter the temperature: ")

    scale = input("Please enter 'C' for Celcius, or 'K' for Kelvin: ")

    if degree > ("99") and scale == "C":
        print("At this temperature, water is a gas.")
    if degree >= ("373.15") and scale == "K":
        print("At this temperature, water is a gas.")
          
    if degree <= ("0") and scale == "C":
        print("At this temperature, water is a solid.")
    if degree <= ("273.15") and scale == "K":
        print("At this temperature, water is a solid.")
    
    else:
        print("At this temperature, water is a liquid.")
   

main()
