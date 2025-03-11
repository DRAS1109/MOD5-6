"""
Trabalho Modelo - Módulo 6
--------------------------
Um programa para gerir livros e empréstimos de uma biblioteca
Requesitos funcionais:
    - Gestão Livros (CRUD)
    - Gestão leitores (CRUD)
    - Empréstimos e devoluções
    - Estatísticas (Empréstimos em atraso, Top Livros, Top Mês, Top Leitores, ...)

"""
import Utils
import Livros

def MenuPrincipal():
    Op = 0
    while Op != 5:
        Op = Utils.Menu(["Livros", "Leitores", "Empréstimos / Devoluções", "Estatísticas", "Sair"], "Menu Principal")
        print("")

        if Op == 5:
            break

        if Op == 1:
            Livros.MenuLivros()

if __name__ == "__main__":
    MenuPrincipal()