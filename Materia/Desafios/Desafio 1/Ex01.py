Notas = {"Aluno 1": {"PT": 0, "ING": 0, "AI": 0, "TIC": 0, "Media": 0},
         "Aluno 2": {"PT": 0, "ING": 0, "AI": 0, "TIC": 0, "Media": 0}}

for Aluno in Notas:
    Soma = 0
    for Disciplina in Notas[Aluno]:
        #Input das notas e colocar no dicionario
        Nota = float(input(f"Introduza a nota de {Disciplina} de {Aluno}"))
        Notas[Aluno][Disciplina] = Nota

        #Calcular a soma, a media e colocar no dicionario
        Soma += Nota
    Media = Soma / len(Notas[Aluno] - 1) #(len(Notas[Aluno] - 1) dá o nº de disciplinas sem contar a media
    Notas[Aluno][Disciplina] = round(Media, 2)

#Apresentar os dados
for Aluno in Notas:
    print("")
    for Disciplina in Notas[Aluno]:
        print(f"Anulo: {Aluno} | {Disciplina}: {Notas[Aluno][Disciplina]}")

#Mostrar a média dos 2 alunos
print(f"Media dos 2 alunos: {round(((Notas["Aluno 1"]["Media"] + Notas["Aluno 2"]["Media"])/2) ,2)}")