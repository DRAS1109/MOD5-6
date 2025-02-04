Dicionario1 = {"A": 1, "B": 2, "C": 3}
Dicionario2 = {"C": 4, "D": 5}

def Juntar_V1():
    Dicionario1.update(Dicionario2) #Adiciona as chaves novas 
                                    #No caso de ter 2 chaves iguais atualiza o seu valor com o que está á direita

    print(Dicionario1)
    print(Dicionario2)

def Juntar_V2():
    #Juntar 2 dicionarios (outra forma)
    DicionarioA = {"A": 1, "B": 2, "C": 3}
    DicionarioB = {"C": 4, "D": 5}

    "O operador | só existe a partir da versão 3.9 do python"

    Juntar = DicionarioA | DicionarioB  #Cria um novo dicionario com o conteudo dos 2 
                                        #No caso de ter 2 chaves iguais atualiza o seu valor com o que está á direita

    print(Juntar)
    print(DicionarioA)
    print(DicionarioB)

Juntar_V2()