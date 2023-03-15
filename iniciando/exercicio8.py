nome = input("Digite seu nome: ")
num = len(nome)
cont = 0
a = ''

while cont < num:
    b = nome[cont]
    a = a + '*' + b
    cont +=1
    

print (a)