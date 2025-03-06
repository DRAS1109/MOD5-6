import random
Numeros = [*range(1,50 + 1)]
Estrelas = [*range(1,12 + 1)]

print("Numeros:")
for i in range (5):
    X = random.choice(Numeros)
    Numeros.remove(X)
    print(X)

print("Estrelas:")
for i in range (2):
    X = random.choice(Estrelas)
    Estrelas.remove(X)
    print(X)