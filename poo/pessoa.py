import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
caminho = 'pessoa1.json'
maria = {'nome': 'maria', 'idade': 20}
p1 = Pessoa('maria',20)
p2 = Pessoa('joão',30)
pe = [vars(p1),vars(p2)]
with open (caminho, 'w', encoding='utf8') as arquivo: 
    json.dump(pe, 
              arquivo,
              ensure_ascii=False,
              indent=2,
            )

