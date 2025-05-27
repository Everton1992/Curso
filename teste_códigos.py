print(" -Selecione seu Número- ") 

import random 

print("selecione um número:") 

num=int(input("")) 

numero_aleatorio = random.randint(1, 6) 

print(numero_aleatorio) 

if numero_aleatorio==num:{ 

    print("POW!"): 

    print("Você perdeu.") 

} 

else:{ 

    print("Parabéns, você ganhou!") 

} 