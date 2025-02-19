"""
Ler do utilizador uma frase e contar quantas palavras unicas tem essa frase 
Passos:
Ler o texto do utilizador
Lista das palavras
Converter lista em set
len para contar
"""

Frase_Teste = "O João e o António foram à casa de banho e depois desapareceram"

Frase = input("Introduza uma frase: ")

Palavras = Frase.split()

Palavras_Unicas = set(Palavras)

print(f"A sua frase tem {len(Palavras)} palavras.")

