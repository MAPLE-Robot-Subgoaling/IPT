def main():
    num_temp = int(input("Please enter the Temperature:"))
    scale_nam = input("Please enter 'C' for Celsius, or 'K' for Kelvin:")
    if scale_nam == 'C' and num_temp <= 0 or scale_nam == "K" and num_temp <= 273:
        print ("At this Temperature water is solid(frozen)")
    elif num_temp < 100 or num_temp < 373:
        print ("At this Temperature water is a liquid!")
    elif num_temp > 100 or num_temp > 373:
        print("At this Temperature water is a gas.")
main() 
