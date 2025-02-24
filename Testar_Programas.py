"""
#Programa para testar a função Menu
#1) Adicionar
#2) Remover
#3) Listar
#4) Terminar


import Utils

while True:
    Op = Utils.Menu(("Adicionar", "Remover", "Listar", "Terminar"), "Menu Principal")
    if Op == 4:
        print("Foi bom conhecer-te\n")
        break

    elif Op == 1:
        print("Não quero adicionar\n")
    
    elif Op == 2:
        print("Não quero remover\n")
    
    elif Op == 4:
        print("Não quero listar\n")"""