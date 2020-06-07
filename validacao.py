def validaInt(txt=''):
    erro = True
    while erro:
        erro = False
        try:
            inteiro = int(input(f'Digite a {txt} idade da pessoa: '))
        except:
            erro = True
            print('ERRO! digite apenas números inteiros!')
    return inteiro
