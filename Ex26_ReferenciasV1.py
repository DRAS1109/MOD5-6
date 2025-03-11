Alunos = [{"Nº Processo": 123, "Nome": "Maria", "Email": "Maria@gmail.com"},
          {"Nº Processo": 124, "Nome": "Joaquim", "Email": "Joaquim@gmail.com"},
          {"Nº Processo": 125, "Nome": "António", "Email": "António@gmail.com"},
          {"Nº Processo": 126, "Nome": "Jorge", "Email": "Jorge@gmail.com"}]

Notas = [{"Nº Processo": 123, "Notas": [12, 13, 14, 15]},
         {"Nº Processo": 124, "Notas": [13, 14, 15, 16]},
         {"Nº Processo": 125, "Notas": [14, 15, 16, 17]}]

#Mostrar o Nome e as notas dos alunos
#Os alunos sem notas não devem aparecer

for Nota in Notas:
    for Aluno in Alunos:
        if Nota["Nº Processo"] == Aluno["Nº Processo"]:
            print(f"{Aluno["Nome"]}: {Nota["Notas"]}")

"""
Considerações:
    - O que deve acontecer se apagar o aluno 124? Apagar também as notas ou não deixar apagar o aluno?
    - Podemos adicionar as notas do aluno 129?
    - Não devemos deixar alterar o Nº Processo
"""