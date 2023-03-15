
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

time = input("Digite a hora: ")
time_float = float(time)
dia = time_float >= 0 and time_float <= 11
tarde = time_float >= 12 and time_float <= 17
noite = time_float >= 18 and time_float <= 23
if dia:
    print("Bom dia!")
elif tarde:
    print("Boa tarde!")
elif noite:
    print("Boa noite!")
else:
    print("Horário inválido")
