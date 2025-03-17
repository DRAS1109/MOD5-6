"""
Modulo Emprestimos e devolocoes
"""
import Utils

def MenuEmprestimos():
    Op = 0
    while Op != 3:
        op = Utils.Menu(["Empréstimos", "Devolução", "Voltar"], "Menu de Empréstimos / Devoluções")

        if Op == 3:
            break

        if Op == 1:
            Emprestimo()

        if Op == 2:
            Devolocao()

def Emprestimo():
    pass
    # Ler qual o livro a emprestar
    # Verificarse o livro pode ser emprestado
    # Ler qual o leitor que leva o livro
    # Verificar se o leitor pode levar o livro
    # Registar o empréstimo com data de devolução
    # Atualizar o estado do livro


def Devolocao():
    pass