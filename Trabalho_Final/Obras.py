"""
Modulo de gestão de obras
"""
import Utils
from datetime import datetime 

#Lista das obras:
Colecao = []

#Menu Obras
def MenuObras():
    """SubMenu para as obras"""

    while True:
        Op = Utils.Menu(["Adicionar", "Editar", "Apagar", "Listar", "Pesquisar", "Voltar"], "Menu de Obras")
        print("")

        if Op == 6:
            break

        if Op == 1:
            Adicionar()

        if Op == 2:
            Editar()
        
        if Op == 3:
            Apagar()

        if Op == 4:
            Listar()
        
        if Op == 5:
            Pesquisar()

#Adicionar
def Adicionar():
    Utils.F_Titulo("Adicionar nova obra")

    #Tipo
    Tipo = Utils.Ler_Strings(2, "Qual o tipo da obra? ")

    #Ano
    Str_Data_Atual = Data()
    Ano_Atual = int(Str_Data_Atual[0])
    Ano = Utils.Ler_Inteiro_Limites(None, Ano_Atual, "Introduza o ano criação da obra: ")

    #Autor
    Autor = Utils.Ler_Strings(2, "Qual o autor da obra? ")

    #Preço Atual
    Preco_Atual = Utils.Ler_Strings(2, "Qual o preço atual da obra? ")

    #Raridade
    Raridade = Utils.Ler_Strings(2, "Qual a raridade da obra? ")

    #Descrição
    Descricao = Utils.Ler_Strings(2, "Introduza uma pequena descrição da obra: \n")

    #Id
    Id = 1
    if len(Colecao) > 0:
        Id = Colecao[len(Colecao) - 1]["Id"] + 1 #Gera o id a partir do id da ultima obra

    Nova_Obra ={"Id": Id,
                "Tipo": Tipo,
                "Ano": Ano,
                "Autor": Autor,
                "Preco Atual": Preco_Atual,
                "Raridade": Raridade,
                "Descricao": Descricao}
    
    Colecao.append(Nova_Obra)
    print(f"Obra registada com sucesso. Tem {len(Colecao)} obras no seu Museu \n")


#Editar
def Editar():
    pass

#Apagar
def Apagar():
    pass

#Listar
def Listar2():
    Utils.F_Titulo("Lista de Obras")
    print(100*"-")
    for Obra in Colecao:
        print(f"| Id: {Obra["Id"]} | Tipo: {Obra["Tipo"]} | Ano: {Obra["Ano"]} | Autor: {Obra["Autor"]}")
        print(100*"-")

def Listar(Colecao):
    """Função para listar os campos (Id, Tipo, Ano, Autor) de todas as obras"""
    #Dicionario para guardar os campos e o comprimento da maior palavra de cada campo
    Campos = {"Id": 0, "Tipo": 0, "Ano": 0, "Autor": 0} 

    #Determinar a maior palavra de cada campo
    for Obra in Colecao:
        for Campo in Obra:
            if len(str(Obra[Campo])) > Campos[Campo]:
                Campos[Campo] = len(str(Obra[Campo])) #Guardar o tamanho da maior palavra de cada campo

    #Imprimir Titulo
    Utils.F_Titulo("Lista de Obras")

    #Imprimir os dados
    print(f" {120*"-"}")
    for Obra in Colecao:
        for Campo in Campos:
            print(f" {Campo}: {Obra[Campo]} {" " * (Campos[Campo] - len(str(Obra[Campo])))}", end="|")
        print("\n", 120*"-")

#Pesquisar
def Pesquisar():
    pass

#Configurar
def Configurar():
    Exemplo_Obras = [
    {"Id": 1, "Tipo": "Livro", "Ano": "1984", "Autor": "O melhor", "Preco Atual": 15.99, "Raridade": "Comum", "Descricao": "Um clássico da ciencia."},
    {"Id": 2, "Tipo": "Moeda", "Ano": "1675", "Autor": "Julio César", "Preco Atual": 1390.26, "Raridade": "Raro", "Descricao": "Uma moeda Romana"},
    {"Id": 3, "Tipo": "Pintura", "Ano": "1214", "Autor": "Leonardo Da Vinci", "Preco Atual": 1394300, "Raridade": "Super Raro", "Descricao": "Uma rara pintura de Leonardo Da Vinci"}]

    #Adicionar as obras
    Colecao.extend(Exemplo_Obras) #append adiciona, extend junta

def Data():
    Data_Atual = datetime.now()
    Str_Data_Atual = Data_Atual.strftime("%Y-%m-%d")
    return Str_Data_Atual

#Lista das caracteristicas
def Caracteristicas():
    pass