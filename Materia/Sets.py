"""
Sets (conjuntos)
Únicos(Os elementos repetidos são descartados), não ordenados(não tem ordem fixa),
mutaveis(adicionar, remover), elementos imutaveis(bool, int, float, string)
"""

#Definir set
Nomes_1={"Dinis","Miguel"}
Nomes_2={"Samuel","Francisco","Gabriel","Dinis"}
Nomes_3={"Miguel","Dinis"}

#Funçoes basicas
Nomes_3.add("Afonso")
print(Nomes_3)

Nomes_3.remove("Afonso")
print(Nomes_3)

#Igualdade
if Nomes_1==Nomes_3:   #Iguais porque a ordem a ordem dos elementos não conta
    print("São Iguais")
else:
    print("São diferentes")

#União
nomes=Nomes_1.union(Nomes_2)#Faz a união e devolve sem alterar
print("União:",nomes)
nomes_v2=Nomes_1|Nomes_2    #Faz a união e devolve sem alterar
print("União:",nomes_v2)
Nomes_1.update(Nomes_2)     #Faz união e altera
print("União:",Nomes_1)

#Interseção
nomes_iguais=Nomes_3.intersection(Nomes_1)  #devolve a interseção sem alterar
print("Interseção:",nomes_iguais)
nomes_iguais_2=Nomes_3&Nomes_1              #devolve a interseção sem alterar
print("Interseção:",nomes_iguais_2)
Nomes_1.intersection_update(Nomes_3)        #Faz a interseção alterando
print("Interseção:",Nomes_1)

#Diferença
diferenca=Nomes_3.difference(Nomes_2)         
print(f"{Nomes_3} - {Nomes_2}=> Diferença:",diferenca)
diferenca=Nomes_2.difference(Nomes_3)         
print(f"{Nomes_2} - {Nomes_3}=> Diferença:",diferenca)
diferenca = Nomes_2 - Nomes_3                      
print(f"{Nomes_2} - {Nomes_3}=> Diferença:",diferenca)

#Diferença Simétrica
diferenca_simetrica= Nomes_3.symmetric_difference(Nomes_2)   
print(f"{Nomes_2} - {Nomes_3}=> Diferença Simétrica:",diferenca_simetrica)
diferenca_simetrica = Nomes_2 ^ Nomes_3
print(f"{Nomes_2} - {Nomes_3}=> Diferença Simétrica:",diferenca_simetrica)

#Converter
valores=set([2,3,10,4,22,24,22])   #Converte uma lista em set
print(valores)

#Listar os valores
for elemento in Nomes_2:
    print(elemento)

"print(valores[1])" #Não funciona, da erro

for p ,valor in enumerate(valores,start=1):
    print(f"Elemento da posição {p}: {valores}")

#Testar se existe

if 2 in valores:
    print("Existe o valor 2")
else:
    print("Não existe o valor 2")