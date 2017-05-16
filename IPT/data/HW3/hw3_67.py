
def main():
    temp = float(input("please enter the temperature: "))
    form =  input("please enter 'C' for celsius or 'K' for kelvin: ")
    

    if(temp > 0) and ( temp < 100) and (form == "C"):
      print("the water is a liquid.")               
    if(temp <= 0) and (form == "C"):
      print("the water is frozen solid.")               
    if(temp >=100) and (form == "C"):
      print("the water is a gas.") 


    if(temp > 273) and (temp < 373) and (form == "K"):
        print("the water is a liquid")
    if(temp <= 273) and (form == "K"):
        print("the water is frozen solid")
    if(temp >= 373) and (form == "K"):
        print("the water is a gas.")

main()
