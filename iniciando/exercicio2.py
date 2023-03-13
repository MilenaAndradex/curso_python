#calculo IMC

nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = peso / (altura * altura) 

print("{} tem {} de altura, pesa {} quilos e seu IMC é {:.2f}".format(nome, altura, peso, imc))