"""
Programa para gerir os livros de uma biblioteca e os emprestimos
Menu:
1) Adicionar livro (Nome: | Tema: | Leitor: None | Data_Emp: None)
2) Listar livro
3) Emprestar
4) Devolução
5) Terminar
"""

import numpy as np
from datetime import datetime

def Contar(Max_Livros, Biblioteca):
    """Devolver o Nº de posições preenchidas do array"""

    for P in range (Max_Livros):
        if Biblioteca[P] == None:
            return P
    
    return Max_Livros

def Livro():
    """Criar um dicionario para o Livro"""
    Nome = input("Introduza o nome do livro: ")
    Tema = input("Introduza o tema do livro: ")
    Leitor = None
    Data_Emp = None

    return {"Nome": Nome,
            "Tema": Tema,
            "Leitor": Leitor,
            "Data_Emp": Data_Emp}

def Adicionar(Max_Livros, Biblioteca):
    """Função para adicionar um novo livro ao Array"""
    Posição = Contar(Max_Livros, Biblioteca)

    if Posição == Max_Livros: #Verificar se o Array está cheiro
        print("Não pode inserir mais dados")
        return
    
    Novo_Livro = Livro()

    Novo_Livro["Id"] = Posição + 1

    Biblioteca[Posição] = Novo_Livro #Adicionar o novo livro ao array


def Listar(Biblioteca):
    for Livro in Biblioteca:
        if Livro != None:
            print(Livro)
        
        else:
            return

def Emprestimo(Max_Livros, Biblioteca):
    """Função para emprestar um livro"""
    Id = int(input("Introduza o Id do livro a emprestar: "))

    if Id < 1 or Id > Contar(Max_Livros, Biblioteca): #Validar Id
        print("O Id introduzido não é válido")
        return

    #Verificar se o livro ja está emprestado
    Posicao = Id - 1

    if Biblioteca[Posicao]["Leitor"] != None:
        print(f"Este livro ja está emprestado ao leitor: {Biblioteca[Posicao]["Leitor"]}")
        return

    #Completar as informações do emprestimo
    Leitor = input("Introduza o nome do leitor: ")
    Data = datetime.now().strftime("%d-%m-%Y")

    Biblioteca[Posicao]["Leitor"] = Leitor
    Biblioteca[Posicao]["Data_Emp"] = Data

    print("Livro emprestado com sucesso")


def Devolução(Max_Livros, Biblioteca):
    """Função para emprestar um livro"""
    Id = int(input("Introduza o Id do livro devolvido: "))

    if Id < 1 or Id > Contar(Max_Livros, Biblioteca): #Validar Id
        print("O Id introduzido não é válido")
        return

    #Verificar se o livro ja está emprestado
    Posicao = Id - 1

    if Biblioteca[Posicao]["Leitor"] == None:
        print(f"Este livro não está emprestado")

    #Alterar as informações para a devolução
    Biblioteca[Posicao]["Leitor"] = None
    Biblioteca[Posicao]["Data_Emp"] = None

    print("Livro devolvido com sucesso")


def Menu():
    Max_Livros = 100

    Biblioteca = np.empty(Max_Livros, dtype=object)

    Menu_P = """
    1) Adicionar Livro
    2) Listar Livros
    3) Emprestimo
    4) Devolução
    5) Terminar
"""
    Op = 0

    while Op != 5:
        print(Menu_P)
        Op = int(input("Opção: "))

        if Op == 1:
            Adicionar(Max_Livros, Biblioteca)

        elif Op == 2:
            Listar(Biblioteca)

        elif Op == 3:
            Emprestimo(Max_Livros, Biblioteca)

        elif Op == 4:
            Devolução(Max_Livros, Biblioteca)

        elif Op == 5:
            print("Obrigado por utilizar o nosso programa :D")
            break
            
        else:
            print("Opção inválida")

if __name__ == "__main__":
    Menu()