def Definir():
    #Definir uma lista:
    Lista = [] #Lista vazia
    Lista2 = [1,2,3.5,"Quatro", True]
    Lista3 = list(range(5))
    print(f"{Lista} \n{Lista2} \n{Lista3} \n")

def Copia():
    #Listas são referencias
    X = 10
    Y = X  #Cria uma variavel nova e copia o valor para essa variavel
    X = 11
    print(f"{X} \n{Y} \n")

    ListaX = [1,2,3]
    ListaY = ListaX  #As duas listas apontam para o mesmo conjunto de dados
    ListaX[1] = 10
    print(f"{ListaX} \n{ListaY} \n")

    #Para criar uma cópia da lista
    ListaZ = ListaX[:]  # Cria uma lista nova e copia todos os valores
    ListaX[1] = 5
    print(f"{ListaX} \n{ListaZ} \n")

def Listar():
    ListaZ = [1,2,3] #Listar os valores de uma lista
    print(ListaZ[0], "\n") #Mostra o 1º elemento de uma lista

    for N in ListaZ:
        print(N)
    print("")
    
    for N in range(len(ListaZ)):
        print(ListaZ[N])
    print("")

    ListaL = [1,2,[30, 40]] #Lista com uma lista incorporada
    print(ListaL[2][0], "\n") #Mostra o 1º elemento da lista incorporada

    ListaD = [{"Joaquim": 10, "Maria": 8}, {"Antonio": 16}, "Miguel"] #Lista com uma dicionario incorporado
    print(ListaD[0]["Maria"], "\n") #Mostra a nota da Maria (Dicionario1, Chave:Maria)

def Adicionar():
    Cores = []

    Cores.append("Vermelho") #Adiciona a cor Vermelho

    Cor = input("Introduza uma cor: ")
    Cores.append(Cor)

    Cores.insert(0, "Amarelo") #Insere uma cor na posição 0 (Empurra os outros para a frente)

    print(Cores)

def Remover():
    Cores = ["Vermelho", "Amarelo", "Roxo"]
    Carros = ["Audi", "BMW", "Mercedes", "Ferrari", "Ford"]

    Cores.remove("Vermelho") #Remove o primeiro Vermelho da lista e da erro se não encontrar
    print(Cores)

    Cor_R = Cores.pop(0) #Remove o elemento da posição indicada e da erro se a lista estiver vazia ou não existir a posição
    print(f"Cor removida: {Cor_R}")
    print(Cores, "\n")

    del Carros[1:4] #Remove os elementos da posiçãi 1 a 3 (4 não inclusive)
    print(Carros, "\n")

    Carros.clear() #Limpa a lista

    Carros = [] #Recria a lista (se fizer dentro de uma outra função, cria uma nova vazia)

def Juntar():
    Cores = ["Vermelho", "Amarelo", "Roxo"]
    Carros = ["Audi", "BMW", "Mercedes", "Ferrari", "Ford"]

    Carros.extend(Cores)
    print(Cores)
    print(Carros, "\n")

    Carros_Cores = Carros + Cores
    print(Cores)
    print(Carros)
    print(Carros_Cores, "\n")