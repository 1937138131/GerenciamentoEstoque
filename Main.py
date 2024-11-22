from project.models.Produto import Produto
from project.models.Cliente import Cliente
from project.models.Pedido import Pedido

# Criando produtos
produto1 = Produto(1, "Teclado Mecânico", "Teclado com RGB e switches azuis", 250.0, 10)
produto2 = Produto(2, "Mouse Gamer", "Mouse com 7 botões programáveis", 150.0, 5)

# Criando cliente
cliente = Cliente(1, "Laercio Santos", "laercio@example.com", "+5511999999999")

# Criando pedido
pedido = Pedido(1, cliente, "22/11/2024")

# Adicionando itens ao pedido
print("Adicionando itens ao pedido...")
pedido.adicionarItem(produto1, 2)  # Adiciona 2 unidades do produto1
pedido.adicionarItem(produto2, 1)  # Adiciona 1 unidade do produto2

# Exibindo itens no pedido
print("\nItens no pedido:")
pedido.listarItens()

# Exibindo total do pedido
print(f"\nTotal do pedido: R${pedido.calcularTotal():.2f}")

# Adicionando pedido ao histórico do cliente
cliente.adicionarCompras(pedido)



