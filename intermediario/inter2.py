# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def mult(a):
    def multiplicardor(num):
        return num * a
    return multiplicardor

duplicar = mult(2)
triplicar = mult(3)
quadruplicar = mult(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
        