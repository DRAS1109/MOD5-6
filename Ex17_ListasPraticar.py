"""
Programa para ler as MArcas de carros de um stand.
O programa deve mostrar qual a marca com mais veiculos
- Ler do Utilizador quando ele inserir uma marca vazia
- Parar de ler quando ele inserir uma marca vazia
- Calcular para cada uma marca quantos carros existem
- Mostrar marca com mais carros
"""
Carro = " "
Carros_L = []
Carros_D = {}


while True:
    Carro = input("Marca: ")

    if Carro == "":
        break

    Carros_L.append(Carro)
    Carros_D[Carro] = 0

#Com dicionario
"""
Maior = 0

for Carro in Carros_L:
    Carros_D[Carro] = Carros_D[Carro] + 1

for Carro in Carros_D:
    print(f"{Carro}: {Carros_D[Carro]}")

    if Carros_D[Carro] > Maior:
        Maior = Carros_D[Carro]
        Maior_C = Carro

print(f"Carro mais repetido: {Maior_C} com {Maior} carros")
"""

#Com Sets
Carros_S = set(Carros_L)
Maior = 0

for Carro in Carros_S:
    print(f"{Carro}: {Carros_L.count(Carro)}")

    if Carros_L.count(Carro) > Maior:
        Maior = Carros_L.count(Carro)
        Maior_C = Carro

print(f"Carro mais repetido: {Maior_C} com {Maior} carros")