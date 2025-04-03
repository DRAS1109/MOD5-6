"""
Trabalho final - Módulo 6
--------------------------
Um programa para gerir livros e empréstimos de uma biblioteca
Requesitos funcionais:
    - Gestão de Obras (CRUD)
    - Gestão de Visitas (CRUD)
    - Estatísticas (Valor total da coleção, Top items mais valiosos, Horarios mais visitados, ...)

Utilizar set:
    - caracterisicas (Tipos)
"""
import Utils, Obras, Visitas, Estatisticas
import os

#Deve estar True quando em testes e False quando em produção
DEBUG = True

def MenuPrincipal():
    if DEBUG:
        Obras.Configurar()
        Visitas.Configurar()

    while True:
        os.system("cls")
        Op = Utils.Menu(["Obras", "Visitas", "Estatísticas", "Sair"], "Menu Principal")
        print("")

        if Op == 4:
            Utils.F_Titulo("Criado por Dinis Sousa")
            os.system("cls")
            break
            
        if Op == 1:
            Obras.MenuObras()
        
        if Op == 2:
            Visitas.MenuVisitas()
        
        if Op == 3:
            Estatisticas.MenuEstatisticas()

if __name__ == "__main__":
    MenuPrincipal()