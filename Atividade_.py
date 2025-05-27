temperatura_agua = 80
temperatura_agua = float(input("digite a temperatura"))
if temperatura_agua > 80:
    print('Preparar')
elif temperatura_agua <= 55:
    print('Não preparar o Chimarrão')
else:
    print('Preparar o Chimarrão')