primeiro_valor = input('Digite um valor:')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print('primeiro valor: {} é maior que o segundo valor: {}' .format(primeiro_valor, segundo_valor))

elif segundo_valor > primeiro_valor:
    print('segundo valor: {} é maior que o primeiro valor: {}' .format(segundo_valor, primeiro_valor))

elif primeiro_valor == segundo_valor:
    print('primeiro valor: {} e segundo valor: {} são iguais' .format(primeiro_valor, segundo_valor))

