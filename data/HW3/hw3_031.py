def main ():
	MELTING_POINT_CELSIUS = 0.0
	MELTING_POINT_KELVIN  = 273.15
	BOILING_POINT_CELSIUS = 100.0
	BOILING_POINT_KELVIN = 373.15
	temperature = float (input ("Please enter the temperature: "))
	scale = input ("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
	if scale.upper() == "C":
		if temperature < MELTING_POINT_CELSIUS:
			print ("Water is a (frozen) solid at this temperature.")
		elif temperature == MELTING_POINT_CELSIUS:
			print ("Water is beginning to freeze. It can be both a solid and liquid at this temperature.")
		elif temperature < BOILING_POINT_CELSIUS:
			print ("Water is a liquid at this temperature.")
		elif temperature == BOILING_POINT_CELSIUS:
			print ("Water is beginning to boil. It can be both a liquid and gas at this temperature.")
		elif temperature > BOILING_POINT_CELSIUS:
			print ("Water is a gas at this temperature.")
	else:
		if temperature < MELTING_POINT_KELVIN:
			print ("Water is a (frozen) solid at this temperature.")
		elif temperature == MELTING_POINT_KELVIN:
			print ("Water is beginning to freeze. It can be both a solid and liquid at this temperature.")
		elif temperature < BOILING_POINT_KELVIN:
			print ("Water is a liquid at this temperature.")
		elif temperature == BOILING_POINT_KELVIN:
			print ("Water is beginning to boil. It can be both a liquid and gas at this temperature.")
		elif temperature > BOILING_POINT_KELVIN:
			print ("Water is a gas at this temperature.")
	print ("Thank you for using the program.")
main ()