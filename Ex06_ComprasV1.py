"""
Pretende-se um programa para calcular o total a pagar por uma lista de compras com base na informação armazenada nas estruturas de dados apresentadas no código, nomeadamente, as listas produtos, precos e quantidades e ainda o dicionário com as percentagens de desconto de cada produto.
"""
Compras = {}

#Produtos comprados
Produtos = ['bananas','maçã','laranja']

#Preços unitários
Precos = [2.5, 3.5, 4.5]

#Quantidades compradas
Quantidades = [2, 3, 3]

#Criar um dicionário que combina os dados das listas produtos, precos e quantidades
Contagem = 0
for Produto in Produtos:
    Compras[Produto] = f"{Precos[Contagem]} | {Quantidades[Contagem]}"
    Contagem = Contagem + 1


#Percentagens de desconto
Descontos={
    'bananas': 0,
    'maçã': 15,
    'laranja': 20
}

#Calcular o valor total a pagar pelas compras tendo em conta as quantidades compradas e percentagem de desconto de cada produto
Pagar = 0
for i in range(len(Produtos)):

    Items_P = Compras[Produtos[i]].split(" | ")
    Preco_P = float(Items_P[0])
    Quant_P = float(Items_P[1])

    Desconto = 1 - (Descontos[Produtos[i]] / 100)
    Pagar = Pagar + (Preco_P * Desconto) * Quant_P

    Pagar = round(Pagar, 2)

#Apresentar o Dicionario e o preço final
for Pares in Compras.items():
        print(f"{Pares[0]} : {Pares[1]}")

print(f"O preço final é: {Pagar}€")