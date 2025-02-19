"""
Calcular o 
(A (interseção) B) / (A (União) B)
"""

FraseA = input("Introduza uma frase: ").strip().lower()
FraseB = input("Introduza uma frase: ").strip().lower()

Conjunto_A = set(FraseA.split())
Conjunto_B = set(FraseB.split())

Interseção = Conjunto_A & Conjunto_B
União      = Conjunto_A | Conjunto_B

Indice = len(Interseção) / len(União)

print(f"Indice: {Indice}")