Alunos = [{"Nº Processo": 123, "Nome": "Maria", "Email": "Maria@gmail.com"},
          {"Nº Processo": 124, "Nome": "Joaquim", "Email": "Joaquim@gmail.com"},
          {"Nº Processo": 125, "Nome": "António", "Email": "António@gmail.com"},
          {"Nº Processo": 126, "Nome": "Jorge", "Email": "Jorge@gmail.com"}]

Notas = [{"Nº Processo": Alunos[0], "Notas": [12, 13, 14, 15]},
         {"Nº Processo": Alunos[1], "Notas": [13, 14, 15, 16]},
         {"Nº Processo": Alunos[2], "Notas": [14, 15, 16, 17]}]

#Mostrar o Nome e as notas dos alunos
#Os alunos sem notas não devem aparecer

del Alunos[0]

for Nota in Notas:
    print(f"{Nota["Nº Processo"]["Nome"]}: {Nota["Notas"]}")

print(Alunos)