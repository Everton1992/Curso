class CadastroCliente():
    def __init__(self, nome, idade, telefone, endereco, e_mail):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.endereco = endereco
        self.e_mail = e_mail

    def mostrar(self):
        print(f'Clinte: {self.nome} \nidade: {self.idade} \nTelefone: {self.telefone} \nEndereço: {self.endereco} \nE-mail: {self.e_mail}')

lista_de_clientes = []

def cadastrar_novo_cliente(lista):
    print('\n--- Cadastrar Novo Cliente ---')

    nome_cliente = input('Digite o nome do cliente: ')
    if nome_cliente.lower == "cancelar":
        print("Cadastro cancelado: ")
        return
       
    while True:
        try:
            idade_cliente = int(input(f'Digite a idade de {nome_cliente}: '))
            if idade_cliente > 0:
                break
            else:
                print('Por favor, digite uma idade válida (número positivo)')
        except ValueError:
            print('entrada inválida, Por favor, digite um número para a idade:')

    telefone_cliente = input(f'Digite o telefone de {nome_cliente}: ')
    endereco_cliente = input(f'Digite o endereço de {nome_cliente}: ')
    email_cliente = input(f'Digite o e-mail de {nome_cliente}: ')

    novo_cliente = CadastroCliente(nome_cliente, idade_cliente, telefone_cliente, endereco_cliente, email_cliente)

    lista_de_clientes.append(novo_cliente)
    print(f"Cliente {novo_cliente.nome} cadastrado com sucesso!")

def mostrar_todos_clientes(lista):   
    print('\n --- Lista de todos os clientes cadastrados ---')
    if not lista_de_clientes:
       print('Nenhum cliente foi cadastrado.')
    else:
       for i, cliente_cadastrado in enumerate(lista_de_clientes):
          print(f'\n--- Cliente {i+1} ---')
          cliente_cadastrado.mostrar()

while True:
    print('\n--- Menu de Cadastro ---')
    print('1.  Cadastrar Novo Cliente: ')
    print('2.  Ver Clientes Cadastrados: ')
    print('3.  Sair: ')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        cadastrar_novo_cliente(lista_de_clientes)

    elif opcao == '2':
        mostrar_todos_clientes(lista_de_clientes)

    elif opcao == '3':
        print('Saindo do sistema...')
        break
    else:
        print('Opção inválida.  Por favor, escolha 1, 2 ou 3.')

print('sistema encerrado!')