from random import randint

numeros = [randint(1,10), randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),
           randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10)]
numerosPrimos = []
numerosNaoPrimos = []

for num in numeros:
    primo = True
    for i in range(2, num):
        if (num%i) == 0:
            primo = False
    if primo:
        numerosNaoPrimos.append(num)
    else:
        numerosPrimos.append(num)

print(numeros)
print(f'Números primos: {numerosPrimos}')
print(f'Números não primos: {numerosNaoPrimos}')