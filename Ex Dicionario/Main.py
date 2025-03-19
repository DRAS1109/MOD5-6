"""
Dicionario funcional
"""

from Dicionario import Configurar, Adicionar, Listar, Pesquisar, Apagar, Ordenar

def Menu(Dicionario):
    if Em_teste:
        Configurar(Dicionario)

    Opções_Menu =   """
1. Adicionar / Editar
2. Listar
3. Pesquisar Palavra
4. Apagar
5. Terminar
"""
    
    Ação = 0

    while Ação != 5:
        Ação = int(input(Opções_Menu))

        if Ação == 5:
            print("Obrigado por utilizar o nosso programa :D")

        elif Ação == 1:
            Adicionar(Dicionario)
        
        elif Ação == 2:
            Dicionario = Listar(Dicionario)
        
        elif Ação == 3:
            Pesquisar(Dicionario)

        elif Ação == 4:
            Apagar(Dicionario)
        
        else:
            print("Opção inválida \t")

def main():
    Dicionario = {}

    Menu(Dicionario)


#Se estiver em testes Em_Teste = True, se não Em_Teste = False
Em_teste = True
main()