from abc import ABC, abstractmethod

# Classe abstrata
class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass  # Método abstrato, deve ser implementado pelas subclasses

# Subclasse concreta
class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

# Subclasse concreta
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14 * (self.raio ** 2)

# Uso
retangulo = Retangulo(5, 10)
circulo = Circulo(7)

print(f"Área do Retângulo: {retangulo.calcular_area()}")  # Saída: 50
print(f"Área do Círculo: {circulo.calcular_area()}")      # Saída: 153.86
