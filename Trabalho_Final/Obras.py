"""
Modulo de gestão de obras
"""
import Utils
from datetime import datetime 

#Lista das obras:
Colecao = []

#Campos que não podem ser editados pelo utilizador
Obras_Campos_Priv = ["Id"] #TODO: Só tem 1 parametro pois futuramente pode ser necessario adicionar mais

#Lista de raridades das obras
Raridades = ["Comum", "Raro", "Epico", "Lendario", "Mitico"]

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
            Listar(Colecao)
        
        if Op == 5:
            Pesquisar_Listar()

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
    Raridade = Utils.Menu(Raridades, "Qual a raridade da obra? ")

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
    #Pesquisar a obra a editar
    Resultado = Pesquisar()

    #Mostrar se não encontrar nenhum livro
    if len(Resultado) == 0:
        print("Não foram encontradas obras com esse critério x_X")
        return
    
    #Mostrar todas as obras encontradas
    Listar(Resultado, None)

    #Se forem varios deixar o utilizador escolher e caso a pesquisa encontre apenas 1, deixar o utilizador cancelar a ação
    Id = Utils.Ler_Inteiro("Introduza o Id da Obra a editar (0 para cancelar): ")
    if Id == 0:
        return
    
    Obra_Encontrada = None #Caso não encontre nenhuma obra, a variavel fica criada
    for Obra in Colecao:
        if Obra["Id"] == Id:
            Obra_Encontrada = Obra
    
    if Obra_Encontrada == None: #Caso não exista nenhuma Obra com o Id indicado (Se estiver a None), alertar o utilizador
        print(f"Não existe nenhuma obra com o id {Id} x_X")
        return
    
    #TODO: Acabar

#Apagar
def Apagar():
    #TODO:
    pass

#Listar
def Listar2():
    """Função Listar mas mais leve"""
    Utils.F_Titulo("Lista de Obras")
    print(100*"-")
    for Obra in Colecao:
        print(f"| Id: {Obra["Id"]} | Tipo: {Obra["Tipo"]} | Ano: {Obra["Ano"]} | Autor: {Obra["Autor"]}")
        print(100*"-")

def Listar(Colecao, Titulo = "Lista de Obras"):
    """Função para listar os campos (Id, Tipo, Ano, Autor) de todas as obras"""
    #Dicionario para guardar os campos e o comprimento da maior palavra de cada campo
    Campos = {"Id": 0, "Tipo": 0, "Ano": 0, "Autor": 0} 

    #Determinar a maior palavra de cada campo
    for Obra in Colecao:
        for Campo in Campos:
            if len(str(Obra[Campo])) > Campos[Campo]:
                Campos[Campo] = len(str(Obra[Campo])) #Guardar o tamanho da maior palavra de cada campo

    #Descobiri o tamanho da linha --------------
    Tamanho = 0
    for Campo in Campos:
        Tamanho += Campos[Campo] + len(Campo)

    #Adicionar à variavel tamanho os "extras" (espaços, : e |)
    Extras = (len(Campos) *2) + (len(Campos) *3) - 1 
        #*2 porque cada campo tem : e espaço E 
        #*3 porque cada campo tem espaço | espaço
        #-1 porque começa com 1 espaço
    Tamanho += Extras  

    #Imprimir Titulo
    Utils.F_Titulo(Titulo)

    #Imprimir os dados
    print(f" {Tamanho*"-"}")
    for Obra in Colecao:
        for Campo in Campos:
            print(f" {Campo}: {Obra[Campo]} {" " * (Campos[Campo] - len(str(Obra[Campo])))}", end="|")
        print("\n", Tamanho*"-")

#Pesquisar
def Pesquisar_Listar():
    """Apresenta lista de obras que correspondem ao critério"""
    Resultado = Pesquisar()
    Listar(Resultado)

def Pesquisar(Titulo = "Escolha o campo de pesquisa: "):
    """Devolve a lista de obras que correspondem ao critério"""
    #Menu para o utilizador escolher o campo de pesquisa
    Op = Utils.Menu(["Tipo","Ano", "Autor", "Raridade"],Titulo)

    #Criar uma lista para os resultados
    L_Resultado = []
    if Op >= 1 and Op <= 3:
        if Op == 1:
            Campo = "Tipo"

        if Op == 2:
            Campo = "Ano"

        if Op == 3:
            Campo = "Autor"

        Pesquisa = Utils.Ler_Strings(1,f"{Campo} a pesquisar: ")
    
    else:
        if Op == 4:
            Campo = "Raridade"
        
        Raridade = Utils.Menu(Raridades, "Qual a raridade da obra? ")
        Pesquisa = Raridades[Raridade - 1]

    #Adicionar à lista as Obras que correspondem ao resultado da pesquisa
    for Obra in Colecao:
        if Pesquisa.lower() in Obra[Campo].lower():
            L_Resultado.append(Obra)

    return(L_Resultado)

#Configurar
def Configurar():
    Exemplo_Obras = [
    {"Id": 1, "Tipo": "Livro", "Ano": "1984", "Autor": "O melhor", "Preco Atual": 15.99, "Raridade": "Comum", "Descricao": "Um clássico da ciencia."},
    {"Id": 2, "Tipo": "Moeda", "Ano": "1675", "Autor": "Julio César", "Preco Atual": 1390.26, "Raridade": "Raro", "Descricao": "Uma moeda Romana"},
    {"Id": 3, "Tipo": "Pintura", "Ano": "1214", "Autor": "Leonardo Da Vinci", "Preco Atual": 1394300, "Raridade": "Epico", "Descricao": "Uma rara pintura de Leonardo Da Vinci"}]

    #Adicionar as obras
    Colecao.extend(Exemplo_Obras) #append adiciona, extend junta

def Data():
    Data_Atual = datetime.now()
    Str_Data_Atual = Data_Atual.strftime("%Y-%m-%d")
    return Str_Data_Atual

#Lista das caracteristicas
def Caracteristicas():
    pass