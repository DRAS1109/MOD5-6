Frutas = {}

for i in range(10):
    Nome = input("Qual o nome da fruta: ")
    Frutas[Nome] = int(input("Qual a quantidade?  "))


for Pares in Frutas.items():
        print(f"{Pares[0]} : {Pares[1]}")

#Eliminar a fruta que menos gosta
Fruta_Proibida = input("Qual a fruta que mais detesta? ")

if Fruta_Proibida in Frutas:
    del Frutas[Fruta_Proibida]
else:
    print(f"Não existe nenhuma fruta aqui chamada: {Fruta_Proibida}")

#Mostrar o nome da fruta com maior quantidade
Maior_F = 0

for Chaves, Valores in Frutas.items():
     if Valores > Maior_F:
          Maior = Chaves
          Maior_F = Valores

print(f"Fruta: {Maior} | Quantidade: {Maior_F}")