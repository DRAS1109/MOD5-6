"""Modulo para estatisticas 
- Raridade mais comum
- Preço da coleção
- Obra mais antiga
- Todos os autores
- Horario mais visitado
"""
import Utils, Obras, Visitas

def MenuEstatisticas():
    """Menu para visitas"""

    while True:
        Op = Utils.Menu(["Raridades", "Valor da coleção","Obra mais antiga", "Todos os autores", "Horario mais visitado", "Voltar"], "Menu de estatisticas")
        print("")

        if Op == 0:
            break

        elif Op == 1:
            E_Raridades()

        elif Op == 2:
            E_Preco()

        elif Op == 3:
            E_Antiga()

        elif Op == 4:
            E_Autores()
        
        elif Op == 5:
            E_Horario()
    

def E_Raridades():
    if len(Obras.Colecao) < 1:
        return
    
    Raridades = {"Comum": 0, "Raro": 0, "Epico": 0, "Lendario": 0, "Mitico": 0}

    #Contar quantas raridades tem a coleção
    for Obra in Obras.Colecao:
        Raridades[Obra["Raridade"]] += 1

    #Encontrar o mais utilizado
    Maior = 0
    for Raridade in Raridades:
        if Raridades[Raridade] > Maior:
            Maior = Raridades[Raridade]
            R_Maior = Raridade

    print(f"A raridade mais comum da coleção é: {R_Maior}, presente em {Maior} Obras")

def E_Preco():
    #Preço total da coleção
    Preco_Total = 0
    for Obra in Obras.Colecao:
        Preco_Total += Obra["Preco Atual"]

    print(f"A coleção tem um preço estimado de {Preco_Total}")

def E_Antiga():
    if len(Obras.Colecao) < 1:
        return

    #Encontrar o mais utilizado
    Antiga = Obras.Colecao[0]["Ano"]
    for Obra in Obras.Colecao:
        if Obra["Ano"] < Antiga:
            Antiga = Obra["Ano"]
            O_Antiga = Obra

    print("Obra mais antiga:")
    print(f"Id: {O_Antiga["Id"]} | Tipo: {O_Antiga["Tipo"]} | Ano: {O_Antiga["Ano"]} | Autor: {O_Antiga["Autor"]} | Preço: {O_Antiga["Preco Atual"]} | Raridade: {O_Antiga["Raridade"]}")
    print(f"Descrição: {O_Antiga["Descricao"]}")

def E_Autores():
    if len(Obras.Colecao) < 1:
        return
    
    Autores = {Obras.Colecao[0]["Autor"]}
    for Obra in Obras.Colecao:
        Autores.add(Obra["Autor"])

    print("Autores de todas as obras da coleção:")
    for Autor in Autores:
        print(f" - {Autor}")

def E_Horario():
    #Verificar se a lotação não está a zero
    Lotacao = False
    for Visita in Visitas.Visitas:
        if Visita["Lotacao"] > 0:
            Lotacao = True

    if Lotacao == False:
        print("Ainda ninguem visitou o seu museu")
        return
    
    #Encontrar o mais visitado
    Maior = 0
    for Visita in Visitas.Visitas:
            if Visita["Lotacao"] > Maior:
                Maior = Visita["Lotacao"]
                R_Maior = Visita["Horario"]

    print(f"O horario mais visitado é: {R_Maior}, com {Maior} visitantes")