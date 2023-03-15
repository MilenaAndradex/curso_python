"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Digite seu nome: ")
num = len(nome)
curto = num < 5
normal = num > 4 and num < 7

if curto:
    print("Seu nome é curto")
elif normal:
    print("Seu nome é mormal")
else:
    print("Seu nome é muito grande")