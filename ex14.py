km = float(input('qual foi a quantidade de km percorrido pelo carro: '))
dias = int(input('por quantos dias ele foi alugado? '))
preco = (dias * 60) + (km * 0.15)
print('O valor a ser pago é de: {}'.format(preco))