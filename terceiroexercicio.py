produtos = {
"Alimentação": [12.50, 8.99, 15.30],
"Limpeza": [5.20, 7.80],
"Higiene": [10.00, 12.00, 9.50, 14.00]
}
medias = {}
for categoria, precos in produtos.items():
    medias[categoria] = sum(precos) / len(precos)

categoriaVencedora = max(medias, key=medias.get)
mediaVencedora = medias[categoriaVencedora]

print(f"Categoria vencedora: {categoriaVencedora}")
print(f"Média: R$ {mediaVencedora:.2f}")