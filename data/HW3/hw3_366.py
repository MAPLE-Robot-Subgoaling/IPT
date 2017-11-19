def main():
	temp = float(input("Please enter the temperature: "))
	if str(input("Please enter 'C' for Celsius of 'K' for Kelvin: ")) == 'C':
		state = "solid" if temp <= 0 else "gas" if temp >= 100 else "liquid"
	else:
		state = "solid" if temp <= 273 else "gas" if temp >= 373 else "liquid"
	print("At this temperature, water is a", state)
main()
