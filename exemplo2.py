def cadastrar_cliente(clientes):
    nome = input("Digite o nome do cliente: ")
    idade = input("Digite a idade do cliente: ")
    email = input("Digite o email do cliente: ")
    
    cliente_id = len(clientes) + 1
    clientes[cliente_id] = {
        'nome': nome,
        'idade': idade,
        'email': email
    }
    print(f"Cliente {nome} cadastrado com sucesso!")