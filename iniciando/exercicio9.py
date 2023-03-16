import os
palavra = 'gato'
secreta = ''
repeticoes = 0

while True:
    letra = input("Digite uma letra: ")
    repeticoes +=1

    if len(letra)> 1:
        print("Digite apenas uma letra")
        continue

    if letra in palavra:
        secreta += letra

    formada =''
    for letr_s in palavra:
        if letr_s in secreta:
            formada += letr_s
        else:
            formada += '*'

    print(formada)

    if formada == palavra:
        os.system('cls')
        print('Parabéns! A palavra era ', palavra)
        print("Numero de tentativas: ",repeticoes)
        break 

    