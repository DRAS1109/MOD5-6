"""
Modulo de Gestão dos livros
"""
import Utils

#Lista dos Livros
Livros = []

#Menu Livros
def MenuLivros():
    """SubMenu para gerir os livros"""

    Op = 0
    while Op != 6:
        Op = Utils.Menu(["Adicionar", "Listar", "Editar", "Apagar", "Pesquisar", "Voltar"], "Menu de Livros")
        print("")

        if Op == 6:
            break

        if Op == 1 :
            Adicionar()

        if Op == 2 :
            Listar(Livros)

        if Op == 3 :
            pass

        if Op == 4 :
            pass

        if Op == 5 :
            Pesquisar()

def Configurar():
    #Lista de Livros de exemplo
    Exemplo_Livros = [
    {"Id": 1, "Titulo": "Livro 1", "Autor": "Autor A", "Assunto": "Assunto 1", "Editora": "Editora A", "Ano": 2001, "Estado": "Disponivel", "Leitor": None, "Nr Emprestimos": 0},
    {"Id": 2, "Titulo": "Livro 2", "Autor": "Autor B", "Assunto": "Assunto 2", "Editora": "Editora B", "Ano": 2002, "Estado": "Disponivel", "Leitor": None, "Nr Emprestimos": 0},
    {"Id": 3, "Titulo": "Livro 3", "Autor": "Autor C", "Assunto": "Assunto 3", "Editora": "Editora C", "Ano": 2003, "Estado": "Disponivel", "Leitor": None, "Nr Emprestimos": 0}]

    """Insere dados de exemplo"""
    Livros.extend(Exemplo_Livros)

#Adicionar Livro
def Adicionar():
    Utils.F_Titulo("Adicionar novo Livro")

    #Titulo
    Titulo = Utils.Ler_Strings(3, "Introduza o título: ")

    #Autor
    Autor = Utils.Ler_Strings(3, "Introduza o autor: ")

    #Assunto
    Assunto = Utils.Ler_Strings(3, "Introduza o assunto: ")

    #Editora
    Editora = Utils.Ler_Strings(3, "Introduza a editora: ")

    #Ano edição
    Ano = Utils.Ler_Inteiro_Limites(1500, 2030, "Introduza o ano de edição: ")

    #Id
    Id = 1
    if len(Livros) > 0:
        Id = Livros[len(Livros) - 1] ["Id"] + 1 #Gera o id a partir do id do ultimo livro

    Novo = {"Id": Id,
            "Titulo": Titulo,
            "Autor": Autor,
            "Assunto": Assunto,
            "Editora": Editora,
            "Ano": Ano,
            "Estado": "Disponivel",
            "Leitor": None,
            "Nr Emprestimos": 0}
    
    Livros.append(Novo)
    print(f"Livro registado com sucesso. Tem {len(Livros)} livros \n")

#Editar Livros

#Apagar Livros

#Listar Livros
def Listar(Livros):
    """Função para listar todos os livros"""
    
    Utils.F_Titulo("Lista de Livros")

    print("-" * 80)
    for Livro in Livros:
        print(f"Id: {Livro["Id"]} | Nome: {Livro["Titulo"]} | Autor: {Livro["Autor"]} | Estado: {Livro["Estado"]} ")
        print("-" * 80)

#Pesquisar Livros
def Pesquisar():
    """Devolver a lista dos livros que correspondem a um critério"""
    #Deixar o utilizador escolher o campo de pesquisa
    Op = Utils.Menu(["Autor","Titulo"],"Escolha o campo de pesquisa: ")

    #Criar uma lista para os resultados
    L_Resultado = []
    if Op == 1:
        Campo = "Autor"
    else:
        Campo = "Titulo"
    Pesquisa = Utils.Ler_Strings(3,f"{Campo} a pesquisar: ")

    #Adicionar à lista os livros que correspondem ao resultado da pesquisa
    for Livro in Livros:
        if Pesquisa.lower() in Livro[Campo].lower():
            L_Resultado.append(Livro)
    Listar(L_Resultado)