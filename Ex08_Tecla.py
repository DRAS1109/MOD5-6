"""
Um programa que utiliza um dicionario para guardar os Professores responsaveis pelas salas do torneio 
do Tecla e o Nº de alunos que cada sala vai ter. As salas são: C5, C6, C7, C8 
O dicionario deve guardar o nome do Professor e o Nº de alunos de cada um.
"""

Tecla = {}#Criar o Dicionario

#Adicionar ao dicionario as salas C5, C6, C7, C8
for Item in range (5, 9):
    Sala = f"C{Item}"
    Professor = input(f"Qual é o porfessoar da sala {Sala}? ")
    Alunos = int(input(f"Quantos alunos vão estar na sala {Sala}? "))
    print(f"Sala adicionada com sucesso! \n")

    Tecla[Sala] = {"Professor":Professor,
                   "Nº Alunos": Alunos}


#Adicionar uma nova sala
Nova_Sala = input("Qual o nome da sala que pretende adicionar? ")
Novo_Professor = input(f"Qual é o porfessoar da sala {Nova_Sala}? ")
Novos_Alunos = int(input(f"Quantos alunos vão estar na sala {Nova_Sala}? "))

print(f"A sala {Nova_Sala} foi adicionada com sucesso! \n")

Tecla[Nova_Sala] = {"Professor":Novo_Professor,
                    "Nº Alunos": Novos_Alunos}

#Remover uma sala
Remover_Sala = input("Qual o nome da sala que pretende remover? (Para cancelar digite: cancelar)")

if Remover_Sala.lower() != "cancelar":
    Sala_Eliminada = Tecla.pop(Remover_Sala, "Não existe nenhuma sala com esse nome")
    print(f"A sala {Remover_Sala} foi removida com sucesso! \n")

else:
    print("Ação cancelada x_x \n")

#Mostrar os items do dicionario Tecla
for Item in Tecla.items():
    print(f"Sala: {Item[0]} | Professor: {Item[1]["Professor"]} | Nº Alunos: {Item[1]["Nº Alunos"]} \n")