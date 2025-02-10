Nomes = ["Joaquim", "João", "Maria"]
Idades = [31, 42, 34]

#Fazer dicionarios com os nomes como Chaves e Idades como Valores
Dicionario = dict(zip(Nomes, Idades))
print(Dicionario)

#Função zip

for Chave, Valor in zip(Nomes, Idades):
    print(f"{Chave} -> {Valor}")