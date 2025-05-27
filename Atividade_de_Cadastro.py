clientes = []
def cadastrar_cliente():
    nome = input('nome: ')
    idade = input('idade: ')
    email = input('e-mail: ')
    cliente = {'nome': nome,
               'idade': idade,
               'e-mail':email}
    
    clientes.append(cliente)
    print('Cliente cadastrado com sucesso!')
        
def lista_clientes():
    if not clientes:
        print('Nenum cliente cadastrado!')
    else:
        print('Lista de clientes cadastrados')
        for i, in enumerate(clientes, star=1):
            print(f'{i}. {clientes ['nome']} | {clientes ['idade']} | {clientes ['e-mail']}')
            print()
            
def buscar_cliente():
    nome_busca = print('Digite o nome do cliente que deseja buscar!').lower()
    encontrados = [c for c in clientes if c['nome'].lower() == nome_busca]
    if encontrados:
        print('Clientes encontrados!')
        for clientes in encontrados:
         print(f'Nome {clientes ['nome']} | {clientes ['idade']} | {clientes ['e-mail']}')
        else:
            print('Cliente não encontrado!')
            print()
            
while True:
    print('--- Menu ---')
    print('1 - Cadastrar novo cliente: ')
    print('2 - lista de cliente: ')
    print('3 - buscar clientes: ')
    print('4 - sair!')
    
    opcao = input('Escolha uma opção: ')
    
    if opcao == '1':
        cadastrar_cliente()
    elif opcao == '2':
        lista_clientes()
    elif opcao == '3':
        buscar_cliente()
    elif opcao == '4':
        print('sair')
        break
    else:
        print(' Opção invalida, tenta novamente')