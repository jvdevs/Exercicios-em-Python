n1 = float(input("Qual foi sua primeira nota: "))
n2 = float(input("Qual foi sua segunda nota: "))
media = (n1 + n2) /2
print('De acordo com suas notas, {} e {}. Sua média ficou {}'.format( n1 , n2 , media))
if media > 7.0:
    print("Parábêns, você foi aprovado")
else:
    print("Poxa, Você foi reprovado, estude mais")