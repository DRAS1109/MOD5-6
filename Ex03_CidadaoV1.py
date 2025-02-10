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
Cidadao = {}
print("Esta a ser hackeado por alianisnas, complete as seguintes informações ou abdusimos uma telha da sua casa")

Cidadao["Nome"]      = str(input("Introduza o seu nome: "))
Cidadao["Morada"]    = str(input("Introduza a sua morada: "))
Cidadao["CP"]        = str(input("Introduza o seu codigo postal (CP): "))
Cidadao["Idade"]     = int(input("Quantos anos tem? "))
Cidadao["Pai"]       = str(input("Introduza o nome do seu pai: "))
Cidadao["Mae"]       = str(input("Introduza o nome da sua mãe: "))
Casado               = str(input("É casado? Sim ou Não?"))
Cidadao["Nr_Filhos"] = int(input("Quantos filhos tem? "))

#Transformar para boleano a chave "Casado"

if Casado in "Ssim":
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