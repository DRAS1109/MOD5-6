"""2. Escreva uma função que receba um dicionário como entrada e retorne a soma de todos os 
valores numéricos."""

def Somar(Dicionario):
    Soma = 0
    for Valor in Dicionario.values():
        Soma = Soma + Valor
    
    return Soma