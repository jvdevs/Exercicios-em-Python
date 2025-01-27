preco = float(input('diga o preço do produto(R$): '))
novo_preco = preco - (preco * 5 / 100) 
print('O preço do produto é {}. Já com o desconto de 5%, fica no valor de {}'.format(preco, novo_preco))