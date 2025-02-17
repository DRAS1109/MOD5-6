"""
Uma familia tem 3 pessoas. Pretende-se um programa que utiliza um dicionario para registar o nome 
de cada um e a marca do respetivo telemovel e computador.
O programa deve indicar qual a marca mais comum e se algum menbro da familia tem somente uma marca
"""

Marcas = {} #Criar dicionario
N_Pessoas = 3

#Preencher dicionario
for _ in range(1, N_Pessoas + 1): 
    Pessoa = input("Qual o nome da pessoa? ")

    Telemovel = input(f"Qual é a marca do telemovel de {Pessoa}? ")
    Computador = input(f"Qual é a marca do computador de {Pessoa}? ")
    print("")

    Marcas[Pessoa] = {"Telemovel": Telemovel,
                      "Computador": Computador}

"""    #Verificar se algum menbro tem somente uma marca
    if Telemovel == Computador:
        print(f"A marca do telemovel e do computador da {Pessoa} são iguais")"""

#Marca mais comum
for i in range (N_Pessoas * (len(Marcas.items()))):
    pass
    #TODO:
        

#Verificar se algum menbro tem somente uma marca
for Marca in Marcas.items():
    if Marca[1]["Telemovel"] == Marca[1]["Computador"]:
        print(f"A marca do telemovel e do computador da {Pessoa} são iguais")