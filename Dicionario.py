"""
Dicionario funcional
"""

def Menu(Dicionario):
    if Em_teste:
        Configurar(Dicionario)


    Opções_Menu = """
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
            Listar(Dicionario)
        
        elif Ação == 3:
            Pesquisar(Dicionario)

        elif Ação == 4:
            Apagar(Dicionario)
        
        else:
            print("Opção inválida \t")

def Configurar(Dicionario):
    Dicionario["Pera"] = "Fruta"
    Dicionario["Pc"] = "Computador Pessoal"
    Dicionario["Bicicleta"] = "Meio de Transporte"
    Dicionario["Ananás"] = "Fruta"


#Se estiver em testes Em_Teste = True, se não Em_Teste = False
Em_teste = True

def Adicionar(Dicionario):
    Palavra = input("Qual palavra quer adicionar ao dicionario? \t")
    Significado = input(f"Qual o significado de {Palavra}? \t")

    if Palavra in Dicionario:
        Ação = input("Essa palavra ja está no dicionario, pretende editar (Sim ou Não)?")

        if Ação.strip().lower() in "naão":
            return
        
    else:
        Dicionario[Palavra] = Significado
        print("Palavra adicionada com sucesso!!")


def Listar(Dicionario):
    Chaves = Ordenar(Dicionario)
    Valores = []

    for i in Chaves: #Criar uma lista de valores com todos os valores ordenados pelas chaves
        Valores = Valores + [Dicionario[i]]

    for i in Dicionario: #Limpar Dicionario
        Dicionario.pop(i)

    Dicionario = dict(zip(Chaves, Valores)) #Junta as Chaves e os valores ja ordenados

    for Pares in Dicionario.items(): #Apresenta todas as palavras e significados
        print(f"{Pares[0]}: {Pares[1]}")


def Pesquisar(Dicionario):
    """Listar(Dicionario)
    Palavra = input("Qual palavra pretende ver? \t")

    Significado = Dicionario.get(Palavra, "Essa palavra não existe")

    print(f"{Palavra}: {Significado}")"""

    #Ler o termo a pesquizar
    Palavra = input("Qual palavra pretende ver? \t")

    #Percorrer Dicionario
    TODO:


def Apagar(Dicionario):
    Listar(Dicionario)

    Palavra = input("Qual palavra pretende apagar? \t")

    if Palavra in Dicionario:
        Ação = input(f"Tem certeza que pretende apagar a palavra: {Palavra}? \t")

        if Ação.strip().lower() in "sim":
            Dicionario.pop(Palavra)

    else:
        print("esta palavra não existe")

def Ordenar(Dicionario):
    Chaves = Dicionario.keys()
    Chaves = Chaves.sorted()

    return Chaves

def main():
    Dicionario = {}

    if __name__ == "__main__":
        Menu(Dicionario)
    
main()