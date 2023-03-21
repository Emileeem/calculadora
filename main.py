conta = int(input(''))
n1 = int(input(''))
n2 = int(input(''))

while True:
    if conta == 1:
        result = emyli.sum(n1,n2)
        break
    elif conta == 2:
        result = benhur.sub(n1,n2)
        break
    elif conta == 3:
        result = emyli.mult(n1,n2)
        break
    elif conta == 4:
        result = benhur.div(n1,n2)
        break
    else:
        print('Escolha uma operção válida')

print('O resultado foi:',result)