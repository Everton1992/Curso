hora_atual = 8
hora_abertura = 9
hora_fechamento = 18

print(f"Hora atual: {hora_atual}")

if hora_abertura <= hora_atual < hora_fechamento:
  print("A loja está aberta.")
else:
  print("A loja está fechada.")