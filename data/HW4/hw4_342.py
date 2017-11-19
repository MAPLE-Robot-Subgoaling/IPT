def main():
    p = float(input("Please enter the starting height of the hailstorm: "))
    while 'true':
       if p == 1:
          print("Hail is stopped at height",p)
          return p
       elif p%2 == 0:
          print("Hail is currently at height",p)
          p = p/2
       else:
          print("Hail is currently at height", p)
          p = 3*p+1
main()
