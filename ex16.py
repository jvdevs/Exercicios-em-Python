from math import hypot

co = float(input("Comprimento do cateteto oposto:"))
ca = float(input("Comprimento do cateteto adjacente:"))
hipo = hypot(co, ca)
print("A hipotenusa é igual a: {}".format(hipo))