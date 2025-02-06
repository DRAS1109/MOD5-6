"""
Dicionario funcional
"""

def Configurar(Dicionario):
    Dicionario["Pera"] = "Fruta"
    Dicionario["Pc"] = "Computador Pessoal"
    Dicionario["Bicicleta"] = "Meio de Transporte"
    Dicionario["Ananás"] = "Fruta"

def Adicionar(Dicionario):
    Palavra = input("Qual palavra quer adicionar ao dicionario? \t")
    Significado = input(f"Qual o significado de {Palavra}? \t")

    if Palavra in Dicionario:
        Ação = input("Essa palavra ja está no dicionario, pretende editar (Sim ou Não)? ")

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

    for i in Chaves: #Limpar Dicionario
        Dicionario.pop(i)

    Dicionario = dict(zip(Chaves, Valores)) #Junta as Chaves e os valores ja ordenados

    for Pares in Dicionario.items(): #Apresenta todas as palavras e significados
        print(f"{Pares[0]}: {Pares[1]}")
        
    return Dicionario


def Pesquisar(Dicionario):
    Palavra = input("Qual palavra pretende ver? \t") #Ler o termo a pesquizar

    #Percorrer Dicionario
    for Chave, Valor in Dicionario.items():
        if Palavra == Chave[:len(Palavra)]:
            print(f"{Chave} -> {Valor}")

    """Significado = Dicionario.get(Palavra, "Essa palavra não existe")
    print(f"{Palavra}: {Significado}")"""


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
    Chaves = sorted(Chaves)
    return Chaves