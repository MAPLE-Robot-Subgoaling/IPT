





def main():
	FREEZING_POINT_K = 273.15
	BOILING_POINT_K = 373.15
	FREEZING_POINT_C = 0
	BOILING_POINT_C = 100
	degrees = float(input("Please enter the temperature: "))
	tempScale = input("Please enter 'C' for Celsius, or 'K' for Kelvin ")
	if tempScale == 'C':
		if degrees <= FREEZING_POINT_C:
			print("At this temperature, water is a (frozen) solid")
		elif degrees <BOILING_POINT_C:
			print("At this temperature, water is a liquid")
		else:
			print("At this temperature, water is a gas")
	else:
		if degrees <= FREEZING_POINT_K:
			print("At this temperature, water is a (frozen) solid")
		elif degrees <BOILING_POINT_K:
			print("At this temperature, water is a liquid")
		else:
			print("At this temperature, water is a gas")

main()
