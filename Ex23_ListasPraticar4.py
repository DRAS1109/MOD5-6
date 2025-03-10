"""
Listas por compreensão
criar uma lista com base num código que gera a lista a partir de outra lista ou uma função geradora
"""
import random

def Carros():
    Lista_Carros = ["Ford", "BMW", "Mercedes", "Renault", "Ferrari"]

    #Criar uma lista dos carros cuja marca começa por f
    Lista_F = []
    for Marca in Lista_Carros:
        if Marca[0] == "f" or Marca[0] == "F":
            Lista_F.append(Marca)


    #Lista aplicando um filtro à lista das marcas
    Lista_F = [ Marca for Marca in Lista_Carros if Marca[0] == "f" or Marca[0] == "F" ]

    print(Lista_F)


def Sorteados():
    Lista_Numeros = [ random.randint(1,1000) for i in range(10)]
    print(Lista_Numeros)

Sorteados()