from Pessoa import Pessoa

lista_de_clientes = []

def cadastrar_novo_cliente(lista_de_clientes):
    print('\n--- Cadastrar Novo Cliente ---')
    
    nome_cliente = input(f'Digite o nome do clinete: ')
    idade_cliente = input(f'Digite a idade de {nome_cliente}: ')
    cpf_cliente = input(f'Digite o CPF de {nome_cliente}: ')
    telefone_cliente = input(f'Digite o telefone de {nome_cliente}: ')
    endereco_cliente = input(f'Digite o endereço de {nome_cliente}: ')
    e_mail_cliente = input(f'Digite o e-mail de {nome_cliente}: ')
    
    novo_cliente = Pessoa(nome_cliente, cpf_cliente, telefone_cliente, idade_cliente, endereco_cliente, e_mail_cliente)
    
    lista_de_clientes.append(novo_cliente)
    print(f'Cliente: {novo_cliente.nome} Cliente cadastrado com sucesso!')
    
def mostrar_todos_clientes(lista_de_clientes):
    print('\n---- Lista de todos os clientes cadastrados---\n')
    if not lista_de_clientes:
        print('Nenhum cliente foi cadastrado!')
    else:
        for i, cliente_cadastrado in enumerate(lista_de_clientes):
            print(f'\n---Cliente: {i+1}---')
            cliente_cadastrado.mostrar()
            
while True:
    print('\n---- Menu De Cadastro ---\n')
    print('1. Cadastrar novo cliente: ')
    print('2. Lista de todos os cliente cadastrados: ')
    print('3. Sair: ')
    
    opcao = input('Digite uma opção: ')
    
    if opcao == '1':
        cadastrar_novo_cliente(lista_de_clientes)
        
    elif opcao == '2':
        mostrar_todos_clientes(lista_de_clientes)
        
    elif opcao == '3':
        print('Saindo do sistema!')
        break
    else:
        print('Opção invalide, tente novamente!')
        
print('Sistema encerrado!')