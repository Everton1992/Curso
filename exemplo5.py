class ProdutoAgro:

    def __init__(self, nome, tipo, preco):
        self.nome = nome
        self.tipo = tipo
        self.preco = preco

    def mostrar(self):
    
        print(f"Produto: {self.nome} {self.tipo} - R${self.preco:.2f}")

print("--- Exibindo Produtos ---")

p1 = ProdutoAgro("Ração para Cães", "Ração", 50.00)
p1.mostrar()

p2 = ProdutoAgro("Ração para Aves", "Ração", 45.50)
p2.mostrar()