import emyli, benhur, maycon

conta = int(input('O que você deseja fazer?\n1-Soma\n2-Subtração\n3-Divisão\n4-Multiplicação\n5-Porcentagem\n:'))
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

while True:
    if conta == 1:
        result = emyli.soma(n1,n2)
        break
    elif conta == 2:
        result = benhur.sub(n1,n2)
        break
    elif conta == 4:
        result = emyli.mult(n1,n2)
        break
    elif conta == 3:
        result = benhur.div(n1,n2)
        break
    elif conta == 5:
        result == maycon.porc(n1,n2)
    else:
        print('Escolha uma operção válida')

print('O resultado foi:',result)
