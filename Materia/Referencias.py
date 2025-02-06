def Ponteiros():
    Dicionario1 = {"A": 1, "B": 2}
    Dicionario2 = {"C": 2, "D": 3}

    Dicionario3 = Dicionario2   #Esta linha não faz uma copia do dicionario2
                                #O dicionario3 é um ponteiro do dicionario2, ou seja, partilham os mesmos dados

    Dicionario3["E"] = 4
    print(Dicionario2)

    Dicionario4 = Dicionario1.copy()
    Dicionario4["Z"] = 10
    print(Dicionario1)

def Referencia_valores():
    Marca1 = {"Nome":"Nike", "Tipo": "Calçado", "Pais": "America"}
    Marca2 = {"Nome":"Adidas", "Tipo": "Roupa e calçado", "Pais": "Alemanha"}
    Marca3 = {"Nome":"Mimosa", "Tipo": "Leite", "Pais": "Portugal"}

    Produto1 = {"Nome": "Sapatilhas", "Preço": 85.43, "Marca": Marca2}

    #Mostrar o Pais da Marca
    print(Produto1["Marca"] ["Pais"])
    Marca2["Pais"] = "Japão"

    print(Produto1)

    Produto2 = {"Nome": "Casaco", "Preço": 100, "Marca": Marca2}

    Marca2 = {} #cria um dicionario novo mas a informação dos produtos continua a ser referenciada

    print(Produto1)
    print(Produto2)

Referencia_valores()

