"""
Um programa que calcula:
-Os alunos que estiveram presentes todos os dias
-Os alunos que faltaram pelo menos 1 dia
-Os alunos que estiveram presentes só na segunda e na sexta
"""

#Conjuntos com os alunos presentes em cada um dos dias
Segunda = {"Ana"  , "Carlos" , "Pedro" , "Maria"}
Terca   = {"Ana"  , "Joao"   , "Pedro" , "Clara"}
Quarta  = {"Maria", "Pedro"  , "Ana"   , "Paulo"}
Quinta  = {"Joao" , "Clara"  , "Paulo" , "Ana"  }
Sexta   = {"Ana"  , "Maria"  , "Carlos", "Paulo"}

Alunos = Segunda | Terca | Quarta | Quinta | Sexta

Todos_Dias = Segunda & Terca & Quarta & Quinta & Sexta
print(f"Alunos que estiveram presentes todos os dias: {Todos_Dias}")

Faltaram1 = Alunos.difference(Todos_Dias)
print(f"Alunos que faltarem pelo menos 1 dia {Faltaram1}")

Segunda_Sexta = Segunda.intersection(Sexta)
Terca_Quarta_Quinta = Terca | Quarta | Quinta
print(f"Alunos que estiveram presentes somente segunda e sexta: {Segunda_Sexta - Terca_Quarta_Quinta}")