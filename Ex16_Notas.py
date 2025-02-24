Notas = {
    "Joaquim": (10, 12, 14, 8 , 15),
    "Maria":   (14, 10, 13, 8 , 15),
    "António": (10, 11, 12, 10, 11)
}

Disciplinas = ("PT", "ING", "MAT", "PSI", "EF")

#Reconstruir o dicionario
Alunos = {}
for Aluno in Notas:
    Alunos[Aluno] = {}
    for Contar in range(len(Disciplinas)):
        Alunos[Aluno][Disciplinas[Contar]] = Notas[Aluno][Contar]
        Alunos[Aluno]["Media"] = 0


#Calcular e mostrar a média das notas de cada aluno
for Aluno in Alunos:
    Soma = 0
    for Disciplina in Alunos[Aluno]:
        Soma = Soma + Alunos[Aluno][Disciplina]

    Media = Soma / len(Alunos[Aluno])
    print(f"A media do aluno {Aluno} é: {round(Media, 2)}")
    Alunos[Aluno]["Media"] = round(Media, 2)

#Mostrar o nome do aluno com maior media
Maior_Media = 0
for Aluno in Alunos:
    if Alunos[Aluno]["Media"] > Maior_Media:
        Maior_Media = Alunos[Aluno]["Media"]
        Maior_Media_Nome = Aluno

print(f"O aluno com a maior media é: {Maior_Media_Nome} com {Maior_Media} valores")


#Mostrar o nº de negativas de cada aluno
for Aluno in Alunos:
    Negativas = 0

    for Disciplina in Alunos[Aluno]:
        if Alunos[Aluno][Disciplina] < 10:
            Negativas = Negativas + 1
        
    if Alunos[Aluno]["Media"] < 10:
        Negativas = Negativas - 1

    if Negativas == 0: #Mostrar o nome dos alunos sem negativas
        print(f"O Aluno {Aluno} não tem negativas")

    else:
        print(f"O aluno {Aluno} tem {Negativas} negativas")


#Calcular e mostrar a média das notas de cada disciplina
for Disciplina in Alunos[Aluno]:
    Soma_Disciplina = 0
    if Disciplina != "Media":
        for Aluno in Alunos:
            Soma_Disciplina = Soma_Disciplina + Alunos[Aluno][Disciplina]

        print(f"A media de {Disciplina} é {round((Soma_Disciplina / len(Alunos)), 2)}")