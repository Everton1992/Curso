estoque = 550
print(f'temos {350} garrafas de vinho em estoque')
vendas = int(input('digite o total de garrafas vendidas hoje? ' ))
resultado = estoque - vendas
print(f'Ainda temos: {resultado} em estoque!')