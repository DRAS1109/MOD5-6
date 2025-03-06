"""
Programa para sugerir uma aposta no euromilhões
Deve sortear 5 Nº entre 1 e 50 sem repetiçoes e 2 Nº entre 1 e 12 também sem repitir
"""

import random

Numeros = set()
Estrelas = set()

while len(Numeros) != 5 or len(Estrelas) != 2:
    if len(Numeros) < 5:
        Numero = random.randint(1,50)
        Numeros.add(Numero)
    
    if len(Estrelas) < 2:
        Numero = random.randint(1,12)
        Estrelas.add(Numero)

print("Chave promissora:")
print(f"Numeros: {Numeros}")
print(f"Estrelas: {Estrelas}")