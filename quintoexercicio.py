numero = input("Digite um número: ")

try:
    num_float = float(numero)

    if num_float % 1 != 0:
        parte_inteira = int(num_float)
        parte_decimal = num_float - parte_inteira
        print(f"Número decimal!")
        print(f"Parte inteira: {parte_inteira}")
        print(f"Parte decimal: {parte_decimal:.10f}")
    else:
        num_inteiro = int(num_float)
        if num_inteiro % 2 == 0:
            print(f"{num_inteiro} é par")
        else:
            print(f"{num_inteiro} é ímpar")

except ValueError:
    print("Erro: O valor digitado não é um número válido!")