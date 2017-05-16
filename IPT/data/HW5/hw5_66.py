
























def box():
    a = int(input('Please enter the width of the box: '))
    b = int(input('Please enter the height of the box: '))
    c = input('Please enter a symbol for the box outline: ')
    d = input('Please enter a symbol for the box fill: ')
    for ii in range(b):
        for i in range(a):
            if ii == 0 or ii == b-1:
                print(c, end='')
        if i == a-1:
            print('')
    if ii == 1:
        for iii in range(1):
            print(c, end='')
        for iiii in range(1,a-1):
            print(d, end='')
        for iii in range(1):
            print(c, end='')
        print('')
box():
