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

#Adicionar Livro

#Editar Livros

#Apagar Livros

#Listar Livros

#Pesquisar Livros