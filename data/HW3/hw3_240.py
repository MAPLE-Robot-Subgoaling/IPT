def main():
	temperature = float(input("Please enter the temperature: "))
	scale = input("Please enter 'C' for Celsius or 'K' for Kelvin: ")
	state = "NONE"
	if (scale == "K"):
		if (temperature >= 373.15):
			state = "gas"
		elif (temperature > 273.15):
			state = "liquid"
		else:
			state = "(frozen) solid"
	elif (scale == "C"):
		if (temperature >= 100.0):
			state = "gas"
		elif (temperature > 0.0):
			state = "liquid"
		else:
			state = "(frozen) solid"
	print("At this temperature, water is a {}.".format(state))
main()
