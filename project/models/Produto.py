class Produto():
    def __init__(self, id:int, nome:str, descricao:str, preco:float, estoque:int):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        
#Metodos
    def atualizarEstoque(self, quantidade:int):
        self.estoque += quantidade
        
    def aplicarDesconto(self, percentual):
        self.preco -= self.preco * (percentual / 100)
    
    