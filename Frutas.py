Frutas = {}

for i in range(10):
    Nome = input("Qual o nome da fruta: ")
    Frutas[Nome] = int(input("Qual a quantidade?  "))


for Pares in Frutas.items():
        print(f"{Pares[0]} : {Pares[1]}")

Fruta_Proibida = input("Qual a fruta que mais detesta? ")

Frutas.pop(Fruta_Proibida, f"Não existe nenhuma fruta aqui chamada: {Fruta_Proibida}")