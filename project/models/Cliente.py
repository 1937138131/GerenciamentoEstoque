class Cliente():
    def __init__(self, id:int, nome:str, email:str, telefone:str):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.historico = []
    
    def adicionarCompras(self, pedido):
        self.historico.append(pedido)
        
    def listarCompras(self):
        for p in self.historico:
            print(f"{p}")