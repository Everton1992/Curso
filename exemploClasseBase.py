class Animal:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor
        
    def emitir_som(self):
        print('Som de animal')
        
    def info(self):
        print(f'Nome: {self._nome}, Idade: {self._idade}')
        
class Cachorro(Animal):
    def emitir_som(self):
        print('Au au!')

class Gato(Animal):
    def emitir_som(self):
        print('Miau!')
        
dog = Cachorro('REX', 5)
cat = Gato('MIMI', 3)

dog.info()
dog.emitir_som()

cat.info()
cat.emitir_som()

cat.nome = 'Luna'
cat.info()
cat.emitir_som()