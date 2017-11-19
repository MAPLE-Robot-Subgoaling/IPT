KELVIN_CONVERT = 273.15
def main():
	temperature = float(input("Please enter the temperature: "))
	scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
	if scale == "K":
		temperature -= KELVIN_CONVERT
	if temperature <= 0:
		print("At this temperature, water is a (frozen) solid.")
	elif temperature >= 100:
		print("At this temperature, water is a gas.")
	else:
		print("At this temperature, water is a liquid.")
main()
