"""
Programa para mostrar a capital de um pais inserido pelo utilizador
"""

Capitais = {"Portugal" : "Lisboa",
            "Espanha" : "Madrid",
            "França" : "Paris",
            "Brasil" : "Brasilia",
            "Inglaterra" : "Londres",
            "Italia" : "Roma"}

#Perguntar o Pais
Pais = input("Qual o Pais da capital que pretende saber: ")

#Mostrar a capital Correspondente V1
if Pais in Capitais:
    print(Capitais[Pais])

else:
    print(f"Não tenho informações sobre o pais: {Pais}")

#Mostrar a capital Correspondente V2
print(Capitais.get(Pais, f"Não tenho informações sobre o pais: {Pais}"))