C_FREEZING_POINT = 0
C_BOILING_POINT = 100
K_FREEZING_POINT = 273.15
K_BOILING_POINT = 373.15
def main():
    temperature = float(input('Please enter the temperature: '))
    scale = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")).lower()
    state = ''
    if scale == 'c':
        if temperature <= C_FREEZING_POINT:
            state = '(frozen) solid.'
        elif temperature >= C_BOILING_POINT:
            state = 'gas. '
        else:
            state = 'liquid.'
    elif scale == 'k':
        if temperature <= K_FREEZING_POINT:
            state = '(frozen) solid.'
        elif temperature >= K_BOILING_POINT:
            state = 'gas.'
        else:
            state = 'liquid.'
    print('At this temperature, water is a', state)
main()
