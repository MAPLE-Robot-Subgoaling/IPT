

def main():
    width=int(input('Please enter the width of the box: ',))
    height=int(input('Please enter the height of the box: ',))
    rim=input('Please enter a symbol for the box outline: ',)
    fill=input('Please enter a symbol for the box fill: ',)
    for i in range(width):
        row=[]
        for j in range(height):
            if i==0 or i==(width-1) or j==0 or j==(height-1):
                row.append(rim)
            else:
                row.append(fill)
        line=''.join(row)
        print(line)
main()
