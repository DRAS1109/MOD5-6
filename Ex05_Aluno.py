import numpy as np

Notas = np.array([12, 10, 11, 14])

Aluno1 = {"Nome": "Joaquim", "Turma": "10T", "Email": "Joaquim@Gmail.com", "Notas": Notas}

#Listar as notas do Aluno 1

for Nota in Aluno1["Notas"]:
    print(Nota)
