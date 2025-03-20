Dicionario = {123: {"Nome": "Carlos"  , "Cidade": "Viseu" , "Visitas": 22},
              124: {"Nome": "Paula"   , "Cidade": "Viseu" , "Visitas": 44},
              125: {"Nome": "Filipa"  , "Cidade": "Porto" , "Visitas": 67},
              126: {"Nome": "Rui"     , "Cidade": "Lisboa", "Visitas": 35},
              127: {"Nome": "Fernando", "Cidade": "Porto" , "Visitas": 165}}

#1 Mostrar os dados ordenados
for Cliente in Dicionario:
    print(Cliente) #Mostrar o codigo do cliente (Exemplo: 124)
    for Visitas in Dicionario[Cliente]:
        print(f"{Visitas} - {Dicionario[Cliente][Visitas]}")
    print("")

#2 Mostrar o nº de visitas correspondente ao código inserido pelo utilizador
Codigo = int(input("Codigo: "))
print(f"O código {Codigo} tem {Dicionario[Codigo]["Visitas"]} visitas. \n")

#3 Adicionar + 1 visita correspondente ao código inserido pelo utilizador
Codigo = int(input("Codigo Visitante: "))
Dicionario[Codigo][Visitas] += 1
print(f"O código {Codigo} passou a ter {Dicionario[Codigo]["Visitas"]} visitas.")

#4 Mostrar a cidade com mais visitantes
Maior = 0
Cidade_Maior = ""
for Chave in Dicionario:
    Temp_Cidade = Dicionario[Chave]["Cidade"]
    Nr_Visitas = Dicionario[Chave]["Visitas"]
    for Codigo in Dicionario:
        if Temp_Cidade == Dicionario[Codigo]["Visita"]:
            Nr_Visitas += Dicionario[Codigo]["Visita"]
    
    if Nr_Visitas > Maior:
        Cidade_Maior = Temp_Cidade
        Maior = Nr_Visitas

print(Cidade_Maior)