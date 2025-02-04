"""
Programa para calcular quantos carros de cada marca existem num array 
Guardando num dicionario a marca e nº de carros
Ex:
    {"BMD":2,
    "Testa":3
    ...}
"""

import numpy as np

Carros = np.array(["Testa", "Polvo", "BMD", "Pejoute", "Testa", "BioAiDi", "Merceres", "BioAiDi"])
Vezes = np.zeros(len(Carros))

Marcas = {}

def V1(Marcas):
    for i in Carros:
        Marcas[i] = 1

    for i in range (len(Carros)):
        for j in range(i + 1, (len(Carros))):
            if Carros[i] == Carros[j]:
                Marcas[Carros[i]] = Marcas[Carros[i]] + 1

def V2():
    for i in Carros:
        Marcas[i] = 0
    
    for i in range (len(Carros)):
        Marcas[Carros[i]] = Marcas[Carros[i]] + 1


V2()
for Pares in Marcas.items():
    print(f"{Pares[0]} : {Pares[1]}")