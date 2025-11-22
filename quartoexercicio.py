def produto_escalar(a, b):
    resultado = 0
    for i in range(len(a)):
        resultado += (a[i]*b[i])
    return resultado

a = [2,3,4]
b = [1,4,6]

for i in range(len(a)):
    print(f'{a[i]} * {b[i]} + ', end='')
print(f' = {produto_escalar(a,b)}')