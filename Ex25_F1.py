'''
PSI - Módulo 6
Coleções - F1
'''
 
GrandePremios = [
    {"Número":  1, "Grande Prémio": "Barém", "Vencedor": "Max Verstappen", "Equipa": "Red Bull Racing-Honda RBPT"},
    {"Número":  2, "Grande Prémio": "Arábia Saudita", "Vencedor": "Max Verstappen", "Equipa": "Red Bull Racing-Honda RBPT"},
    {"Número":  3, "Grande Prémio": "Austrália", "Vencedor": "Carlos Sainz Jr.", "Equipa": "Ferrari"},
    {"Número":  4, "Grande Prémio": "Japão", "Vencedor": "Max Verstappen", "Equipa": "Red Bull Racing-Honda RBPT"},
    {"Número":  5, "Grande Prémio": "China", "Vencedor": "Max Verstappen", "Equipa": "Red Bull Racing-Honda RBPT"},
    {"Número":  6, "Grande Prémio": "Miami", "Vencedor": "Lando Norris", "Equipa": "McLaren-Mercedes"},
    {"Número":  7, "Grande Prémio": "Emília-Romanha", "Vencedor": "Max Verstappen", "Equipa": "Red Bull Racing-Honda RBPT"},
    {"Número":  8, "Grande Prémio": "Mónaco", "Vencedor": "Charles Leclerc", "Equipa": "Ferrari"},
    {"Número":  9, "Grande Prémio": "Canadá", "Vencedor": "Max Verstappen", "Equipa": "Red Bull Racing-Honda RBPT"},
    {"Número": 10, "Grande Prémio": "Espanha", "Vencedor": "Max Verstappen", "Equipa": "Red Bull Racing-Honda RBPT"},
    {"Número": 11, "Grande Prémio": "Áustria", "Vencedor": "George Russell", "Equipa": "Mercedes"},
    {"Número": 12, "Grande Prémio": "Grã-Bretanha", "Vencedor": "Lewis Hamilton", "Equipa": "Mercedes"},
    {"Número": 13, "Grande Prémio": "Hungria", "Vencedor": "Oscar Piastri", "Equipa": "McLaren-Mercedes"},
    {"Número": 14, "Grande Prémio": "Bélgica", "Vencedor": "Lewis Hamilton", "Equipa": "Mercedes"},
    {"Número": 15, "Grande Prémio": "Países Baixos", "Vencedor": "Lando Norris", "Equipa": "McLaren-Mercedes"},
    {"Número": 16, "Grande Prémio": "Itália", "Vencedor": "Charles Leclerc", "Equipa": "Ferrari"},
    {"Número": 17, "Grande Prémio": "Azerbaijão", "Vencedor": "Oscar Piastri", "Equipa": "McLaren-Mercedes"},
    {"Número": 18, "Grande Prémio": "Singapura", "Vencedor": "Lando Norris", "Equipa": "McLaren-Mercedes"},
    {"Número": 19, "Grande Prémio": "Estados Unidos", "Vencedor": "Charles Leclerc", "Equipa": "Ferrari"},
    {"Número": 20, "Grande Prémio": "Cidade do México", "Vencedor": "Carlos Sainz Jr.", "Equipa": "Ferrari"},
    {"Número": 21, "Grande Prémio": "São Paulo", "Vencedor": "Max Verstappen", "Equipa": "Red Bull Racing-Honda RBPT"},
    {"Número": 22, "Grande Prémio": "Las Vegas", "Vencedor": "George Russell", "Equipa": "Mercedes"},
    {"Número": 23, "Grande Prémio": "Catar", "Vencedor": "Max Verstappen", "Equipa": "Red Bull Racing-Honda RBPT"},
    {"Número": 24, "Grande Prémio": "Abu Dhabi", "Vencedor": "Lando Norris", "Equipa": "McLaren-Mercedes"}
]

# Quem ganhou o GP do Brasil
for Dicionario in GrandePremios:
    if Dicionario["Grande Prémio"] == "São Paulo":
        print(f"O vencedor do GP Brasil foi: {Dicionario["Vencedor"]} \n")
        break

# Quais os grandes prémios que ganhou a Ferrari
print("Grandes Prémios da Ferrari:")
for Dicionario in GrandePremios:
    if Dicionario["Equipa"] == "Ferrari":
        print(Dicionario["Grande Prémio"])

print("")

# Quais os Grande Prémios que um determinado piloto ganhou (escolha do utilizador)
Piloto = input("Qual piloto pretende ver os grandes prémios? ")

print(f"O piloto '{Piloto}' ganhou os seguintes prémios:")
for Dicionario in GrandePremios:
    if Dicionario["Vencedor"] == Piloto:
        print(Dicionario["Grande Prémio"])

print("")


# Lista de vencedores (só aparece uma vez)
Vencedores = set()
for Dicionario in GrandePremios:
    Vencedores.add(Dicionario["Vencedor"])

print("Todos os vencedores:")
print(f"{Vencedores} \n")

# Lista de construtores que ganharam provas (só aparece uma vez)
Equipas = set()
for Dicionario in GrandePremios:
    Equipas.add(Dicionario["Equipa"])

print("Todos as Equipas:")
print(f"{Equipas} \n")
 
# Mostrar quantos grandes prémios ganhou cada um desses pilotos
for Piloto in Vencedores:
    Contagem = 0
    for Dicionario in GrandePremios:
        if Dicionario["Vencedor"] == Piloto:
            Contagem = Contagem + 1
    
    print(f"O {Piloto} tem {Contagem} grandes prémios")