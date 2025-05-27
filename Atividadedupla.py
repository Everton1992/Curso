def cadastrar_cliente():
    idade =18
    cliente = []
    """Cadastrar um novo cliente"""
    cliente = {}
    cliente ['nome'] = input('\n Digite o nome: ')
    cliente['idade'] = input('\n Digite a idade: ')
    if idade > 17:
      ('maior de idade!')
    elif idade >= 17:
        print('Menor de idade, solicitar o cadastro de um responssável!')
    cliente['CPF'] = input('\n Digite o CPF: ')
    cliente['telefone'] = input('\n Digite a data de nascimento: ')
    cliente['endereço'] = input('\n digite o endereço: ')
    cliente['telefone'] = input('\n Digite o número de telefone: ')
    cliente['e_mail'] = input('\n Digite o e-mail: ')
    cliente['Profissão'] = input('\n Digite a profissão: ')
    cliente['sexo'] = input('\n Digite o sexo: ')
    cliente['Estado_cívil'] = input('\n Digite estado civil: ')
    return cliente
 
def exibir_clientes(lista_clientes):
 
    """Exibe a lista de clientes cadastrados."""
    if not lista_clientes:
        print("Nenhum cliente cadastrado ainda.")
        return
    print("\n--- Lista de Clientes ---")
    for i, cliente in enumerate(lista_clientes):
        print(f"Cliente {i+1}:")
        for chave, valor in cliente.items():
            print(f"  {chave.capitalize()}: {valor}")
    print("-------------------------\n")
 
lista_de_clientes = []
 
while True:
    print("\n--- Menu de Cadastro de Clientes ---")
    print("1 - Cadastrar um novo cliente")
    print("2 - Exibir lista de clientes")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")
 
    if opcao == '1':
        novo_cliente = cadastrar_cliente()
        lista_de_clientes.append(novo_cliente)
        print("\n Cliente cadastrado com sucesso!")
    elif opcao == '2':
        exibir_clientes(lista_de_clientes)
    elif opcao == '3':
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")