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
import Utils, Livros

#Deve estar True quando em testes e False quando em produção
DEBUG = True

def MenuPrincipal():
    if DEBUG:
        Livros.Configurar()

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