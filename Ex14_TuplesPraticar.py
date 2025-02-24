"""
Exercicios para praticar Tuples
1) Criar um Tuple com os meses do ano
2) Mostrar o 3º mes do ano
3) Obtenha o tuple dos meses de verão (Junho, Julho, Agosto, Setembro)
4) Verifique se Junho está presente nos meses de verão
5) Listar os meses por ordem alfabetica
6) Mostrar os meses cujo nome começa por j
7) Mostrar os mes(es) com o maior nome
"""

Meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", \
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
print("Meses:", Meses)

print("3º Mes:", Meses[3-1])

Verão = Meses[5 : 9]
print("Verão:", Verão)

print("Junho pertence ao Verão?:", "Junho" in Verão)

print(f"Meses ordenados: {sorted(Meses)}")

for Mes in Meses:
    if "J" in Mes:
        print(f"Mes com J: {Mes}")

Maior = Meses[0]
for Mes in Meses:
    if len(Mes) > len(Maior):
        Maior = Mes

Nome_Maior = Maior

for Mes in Meses:
    if len(Mes) == len(Maior) and Mes != Maior:
        Nome_Maior = Nome_Maior + ", " + Mes


print(f"Mes com maior nome: {Nome_Maior}")