from abc import ABC, abstractmethod

class Cliente:
    def __init__(self, nome, cpf, idade, telefone, e_mail, endereco):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.telefone = telefone
        self.e_mail = e_mail
        self.endereco = endereco
        
    @abstractmethod
    def mostrar(self):
        print('Nome: ', self.nome)
        print('CPF: ', self.cpf)
        print('Idade: ', self.idade)
        print('Telefone: ', self.telefone)
        print('E-mail: ', self.e_mail )
        print('Endereço: ', self.endereco)
    
class Pessoa(Cliente):
    def __init__(self, nome, cpf, idade, telefone, e_mail, endereco):
        super().__init__(nome, cpf, idade, telefone, e_mail, endereco)