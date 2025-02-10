"""
Cidadao:
    Nome: str
    Morada: str
    Codigo Postal (CP): str
    Idade:int
    Pai: str
    Mae: str
    Casado: bool
    Nr_Filhos: int

    Filhos:
        -Nome_1º
        -Nome_2º
        ...
"""

Cidadao = {"Nome": "",
           "Morada": "",
           "Codigo Postal (CP)": "",
           "Idade": "",
           "Pai": "",
           "Mae": "",
           "Casado": "",
           "Nr_Filhos": ""}


for Chaves in Cidadao.keys():
        Cidadao[Chaves] = input(f"{Chaves}: ")

#Transformar para inteiros
Cidadao["Idade"] = int(Cidadao["Idade"])
Cidadao["Nr_Filhos"] = int(Cidadao["Nr_Filhos"])

#Transformar para boleano a chave "Casado"
if Cidadao["Casado"] in "Ssim":
    Cidadao["Casado"] = True
else: 
    Cidadao["Casado"] = False

#Inserir o nome dos filhos
for i in range(Cidadao["Nr_Filhos"]):
    Filho = f"{i + 1}º filho"
    Cidadao[Filho] = str(input(f"Qual o nome do seu {Filho}? "))

#Apresentar o dicionario ao utilizador
for Pares in Cidadao.items():
        print(f"{Pares[0]} : {Pares[1]}")