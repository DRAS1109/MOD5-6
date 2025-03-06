Alunos = ["Joaquim", "Antóio", "Maria", "Carlos"]

#Inverter a ordem dos alunos
Alunos = Alunos[::-1]

#Verificar se existem repitidos
if len(Alunos) != len(set(Alunos)):
    print("Há repitidos")

else:
    print("Não há repitidos")