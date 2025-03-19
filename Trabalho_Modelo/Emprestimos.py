"""
Modulo Emprestimos e devolocoes
"""
import Utils, Livros, Leitores
from datetime import datetime, timedelta

#Livro, Leitor, Data_Emprestimo, Data_Devolução, Estado
Emprestimos = []

def MenuEmprestimos():
    Op = 0
    while Op != 3:
        Op = Utils.Menu(["Empréstimos", "Devolução", "Voltar"], "Menu de Empréstimos / Devoluções")

        if Op == 3:
            break

        if Op == 1:
            Emprestimo()

        if Op == 2:
            Devolocao()

def Emprestimo():
    #Dados do emprestimo a adicionar à lista
    Novo = {} 

    # Ler qual o livro a emprestar
    Livro_Emprestar = Livros.Pesquisar("Indique campo de pesquisa do livro a emprestar")

    if len(Livro_Emprestar) == 0:
        print("O livro não foi encontrado, Tente novamente. \n")
        return

    elif len(Livro_Emprestar) > 1:
        #Mostrar livros encontrados
        Livros.Listar(Livro_Emprestar)

        #Pedir o Id do livro a emprestar
        Id = Utils.Ler_Inteiro("Introduza o Id do livro a emprestar: ")

        for Livro in Livro_Emprestar:
            if Livro["Id"] == Id:
                if Livro["Estado"] != "Disponivel":
                    print("Este livro está emprestado. \n")
                    return
                
                Novo["Livro"] = Livro
                break

        if "Livro" not in Novo:
            print("O Id indicado não existe \n")
            return

    else: #Só encontrou 1 livro
        if Livro_Emprestar[0]["Estado"] != "Disponivel":
            print("Esse livro está emprestado. \n")
            return
        Novo["Livro"] = Livro_Emprestar[0]

    # Ler qual o leitor que leva o livro
    Leitor_Emprestimo = Leitores.Pesquisar("Indique o Leitor")

    if len(Leitor_Emprestimo) == 0:
        print("Leitor não encontrado \n")
        return

    elif len(Leitor_Emprestimo) > 1:
        print("leitores encontrados tgthget")
        Leitores.Listar(Leitor_Emprestimo)

        Id = Utils.Ler_Inteiro("Indique o Id do Leitor: ")

        for Leitor in Leitor_Emprestimo:
            if Leitor["Id"] == Id:
                Novo["Leitor"] = Leitor
                break

        if Leitor not in Livro:
            print("O Id indicado não existe. \n")

    else:
        Novo["Leitor"] = Leitor_Emprestimo[0]

    #TODO: Verificar se o leitor pode levar o livro
    # Registar o empréstimo com data de devolução
    Data_Atual = datetime.now()
    Data_Entrega = Data_Atual + timedelta(days=30)

    #Transformar as datas em string
    Str_Data_Atual = Data_Atual.strftime("%Y-%m-%d")
    Str_Data_Entrega = Data_Atual.strftime("%Y-%m-%d")

    #Adicionar ao dicionario a data atual e a data de entrega
    Novo["Data Emprestimo"] = Str_Data_Atual
    Novo["Data Devolução"] = Str_Data_Entrega

    # Atualizar o estado do livro
    Novo["Livro"]["Estado"] = "Esprestado"
    Novo["Livro"]["Leitor"] = Novo["Leitor"]
    print("Emprestimo registado com sucesso :D \n")

def Devolocao():
    """
    Ideias:
    O que acontece se o livro não estiver em condições
    """
    # Ler o Id do Livro a devolver
    Id_Livro = Utils.Ler_Inteiro("Introduza o Id do livro a devolver: ")



    # Verificar se o livro está emprestado
    Livro = Livros.Get_Livro(Id_Livro)
    if Livro == None:
        print("Não existe nenhum livro com o Id indicado \n")

    if Livro["Estado"] != "Emprestado":
        print("Esse livro não está emprestado")

    # Verificar se a devolução está dentro do prazo


    # Registar se houve infração do leitor (entregar o livro estragado ou fora do prazo)
    Tem_Infracao = Utils.Menu(["Sim", "Não"], "Alguma infração do leitor?")

    if Tem_Infracao == 1:
        Infracao = input("Qual foi a infração? ")
    
    # Atualizar o nº de emprestimos do livro
    Livro["Nr Emprestimos"] += 1

    # Mudar o estado do Livro
    Livro["Estado"] = "Disponivel"
    Livro["Leitor"] = None

    # Mudar o estado do emprestimo
