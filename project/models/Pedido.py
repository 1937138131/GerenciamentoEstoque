class Pedido:
    def __init__(self, id: int, cliente, data: str):
        self.id = id
        self.cliente = cliente
        self.data = data
        self.itens = []  # Lista de itens do pedido
        self.total = 0.0  # Total do pedido
    
    def adicionarItem(self, produto, quantidade: int):
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        if produto.estoque < quantidade:
            raise ValueError("Estoque insuficiente para o produto.")
        
        produto.atualizarEstoque(-quantidade)
        
        subtotal = produto.preco * quantidade

        self.itens.append({
            "produto": produto,
            "quantidade": quantidade,
            "subtotal": subtotal
        })
        self.total += subtotal
    
    def removerItem(self, produto):
        for item in self.itens:
            if item["produto"] == produto:
                # Repor o estoque
                produto.atualizarEstoque(item["quantidade"])
                # Atualizar o total do pedido
                self.total -= item["subtotal"]
                # Remover o item
                self.itens.remove(item)
                return
        raise ValueError("Produto não encontrado no pedido.")
    
    def calcularTotal(self) -> float:
        self.total = sum(item["subtotal"] for item in self.itens)
        return self.total
    
    def listarItens(self):
        for item in self.itens:
            produto = item["produto"]
            print(f"Produto: {produto.nome}, Quantidade: {item['quantidade']}, Subtotal: R${item['subtotal']:.2f}")
