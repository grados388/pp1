import math
a=float(input("podaj dlugosc 1 boku: "))
b=float(input("podaj dlugosc 2 boku: "))
c=float(input("podaj dlugosc 3 boku: "))
s=(a+b+c)/2
print(f"pole wynosi: {math.sqrt(s*(s-a)*(s-b)*(s-c))}")