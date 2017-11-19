def main():
 temp = float(input("Enter the temperature: "))
 scale = input("Enter C for celcius and K for Kelvin: ")
 if scale == "K":
     temp = temp - 273.15
 if temp >= 100:
     print("Water is a gas at this temperature. ")
 elif temp <= 0: 
     print("Water is a solid at this temperature. ")
 else:
     print("Water is a liquid at this temperature. ")
main()
