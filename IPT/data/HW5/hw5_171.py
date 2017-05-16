
width = int(input("Please enter width: "))
height = int(input("Please enter height: "))
symbol_outline = input("Please enter a symbol for the outline:") 
symbol_fill = input("Please enter a symbol for the fill:")

def main():
    forl_row = symbol_outline*width
    mid_row = symbol_outline+(symbol_fill*(width-2))+symbol_outline
    print(forl_row)
    for x in range(height):
        print(mid_row)
    print(forl_row)

main()
