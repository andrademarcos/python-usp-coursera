n = int(input('Digite o valor de n: '))

resultado = 1
cont = 1

while cont <= n:
    resultado *= cont
    # resultado = resultado * cont
    cont += 1

print(resultado)