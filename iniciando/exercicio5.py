"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num = input("Digite um número inteiro: ")

try :
    num_int = int(num)
    if num_int % 2 == 0:
        print(f"{num_int} é par")
    else:        
        print(f"{num_int} é ímpar")

except:
    print(f"'{num}' Não é um número inteiro")
    pass
    
