def main():
	print("This program detects the state of matter of water based on the temperature.")
	temp = float(input("Enter the temperature in Celsius or Kelvin:"))
	celsius = "C"
	kelvin = "K"
	choice = input("Enter 'C' for Celsius or 'K' for Kelvin:")
	if choice == celsius:
		if temp < 0:
			print("Solid")
		elif 0 < temp < 100:
			print("Liquid")
		elif temp > 100:
			print("Gas")
	if choice == kelvin:
                if temp < 273.15:
                        print("Solid")
                elif 273.15 < temp < 373.15:
                        print("Liquid")
                elif temp > 373.15:
                        print("Gas")

main()
