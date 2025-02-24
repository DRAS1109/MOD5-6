"""
Utilizando uma função:
Calcular e devolover a soma de todos os vencimentos, o maior e o menor
Calcular e mostrar a média dos vencimentos
Nome da pessoa com maior vencimento
"""

Vencimentos = (1000, 5000, 2500, 1350, 4750, 850)
Nomes       = ("A",  "B",  "C",   "D",  "E",  "F")


def Funções_V(Vencimentos):
    Soma = sum(Vencimentos)
    Maior = max(Vencimentos)
    Menor = min(Vencimentos)

    return Soma, Maior, Menor


def Media_V(Vencimentos, Soma):
    Media = Soma / len(Vencimentos)
    print (f"O vencimento medio é: {Media}")

def Maior_V(Vencimentos, Maior):
    Posicao_Maior = Vencimentos.index(Maior)
    print(f"A pessoa com maior vencimento é: {Nomes[Posicao_Maior]}")


Soma, Maior, Menor = Funções_V(Vencimentos)
print(f"A soma dos vencimentos é: {Soma}")
print(f"O maior vencimento é: {Maior}")
print(f"O menor vencimento é: {Menor}")

Media_V(Vencimentos, Soma)

Maior_V(Vencimentos, Maior)


