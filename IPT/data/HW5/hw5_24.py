


WALL = 2
CONDITION = 1
def main():
    width = int(input("Enter the width "))
    height = int(input("Enter the height "))
    out_sym = input("enter the outer sym ")
    fil_sym = input("enter the inner sym ")
    for i in range(1):
        outer_shell = width * out_sym
        print(outer_shell)
        for i in range(height-WALL):
            var = out_sym + (fil_sym *(width-WALL))+out_sym
            print(var)
        if height != CONDITION:
            print(outer_shell)
main()
