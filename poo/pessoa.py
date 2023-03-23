class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    

maria = {'nome': 'maria', 'idade': 20}
p1 = pessoa(**maria)

print(p1.nome)
print(p1.idade)