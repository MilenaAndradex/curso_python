import os 
lista = []

while True:
    print ("Selecione uma opção")
    i = input("[i]inserir [a]apagar [l]listar:")

    if i == 'i':
        lista.append (input("Item: "))
        os.system('cls')
    
    elif i == "a":
        while True:
            
            a = input("Escolha índice para apagar: ")
            
            if a.isnumeric() == False:
                print ("Valor inválido")
                continue

            b = int(a)
            b -= 1

            if b >= (len(lista)):
                print("Índice não encontrado")
                continue
            else:
                lista.pop(b)
                os.system('cls')
                break

    
    elif i == 'l':
        for item in enumerate(lista, start=1):
            x, z = item
            print(x, z)

        # listaa = enumerate(lista)
        # for letra in lista:
        #     print(letra)
       
    else:
        print("Valor inválido")
        continue
