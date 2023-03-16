# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def mult(*args):
    a = 1
    for num in args:
        a *= num
    return a

b = mult(1,2,3,4,5)
print(b)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def im_par(numero):
    c = numero % 2 == 0
    if c:
        return 'par'
    else: 
        return 'ímpar'

d = im_par(2)
print (d)
e = im_par(3)
print (e)